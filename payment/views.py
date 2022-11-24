from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
import razorpay

from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Account
from teacher_app.models import Course
from .models import StudentEntrollment

from rest_framework.views import APIView
from .serializer import OrderSerializer,FreeOrderSerialzer
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from django.core.mail import send_mail


import json
from rest_framework import status

from .models import StudentEntrollment

from django.conf import settings

# Create your views here.

@api_view(['POST'])
def start_payment(request):
    
    print(request.data)
     # request.data is coming from frontend
    amount = request.data['amount']
    course_id = request.data['course_id']
    student_id =request.data['student_id']

    # setup razorpay client this is the client to whome user is paying money that's you
    client =  razorpay.Client(auth=(settings.PUBLIC_KEY , settings.SECRET_KEY ))
    print('****')

    # create razorpay order
    # the amount will come in 'paise' that means if we pass 50 amount will become
    # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
    # mumtiply it by 100 so it will be 50 rupees.
    payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})
    print(payment)
    # we are saving an order with isPaid=False because we've just initialized the order
    # we haven't received the money we will handle the payment succes in next 
    # function
   
    course =Course.objects.get(pk=course_id)
    student =Account.objects.get(pk=student_id)
    order = StudentEntrollment.objects.create(course=course, 
                                 order_amount=amount, 
                                 student=student,
                                 order_payment_id=payment['id'])

    serializer = OrderSerializer(order)

    """order response will be 
    {'id': 17, 
    'order_date': '23 January 2021 03:28 PM', 
    'order_product': '**product name from frontend**', 
    'order_amount': '**product amount from frontend**', 
    'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
    'isPaid': False}"""

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)



@api_view(['POST'])

def handle_payment_success(request):
    # request.data is coming from frontend
    print('kkk')
    # print(request.data)
    # res = (request.data)
    print("dsfa")
    # print(res)
    res = json.loads(request.data["response"])
    print(res)
    """res will be:
    {'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
    'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
    'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
    this will come from frontend which we will use to validate and confirm the payment
    """

    ord_id = ""
    raz_pay_id = "" 
    raz_signature = ""

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]
    print(ord_id,"loooooo")
    # get order by payment_id which we've created earlier with isPaid=False
    order = StudentEntrollment.objects.get(order_payment_id=ord_id)

    # we will pass this whole data in razorpay client to verify the payment
    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=(settings.PUBLIC_KEY , settings.SECRET_KEY ))

    # checking if the transaction is valid or not by passing above data dictionary in 
    # razorpay client if it is "valid" then check will return None
    check = client.utility.verify_payment_signature(data)
    print(check)
    print(order,'ordo')
    if check is None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    order = StudentEntrollment.objects.get(order_payment_id=ord_id)
    order.isPaid = True
    order.save()
    student_name=order.student.username
    course_name=order.course.title
    teacher_mail=order.course.teacher.email
    send_mail('Hello  ',student_name+
        ' has been Entrolled '+course_name,
        'icart312@gmail.com'
        ,[teacher_mail]   
        )
    print("email sent")

    print('user is',request.user)
    
    
    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)

@api_view(['GET'])
def fetch_entroll_status(request,student_id,course_id):
    student =Account.objects.filter(id=student_id).first()
    course =Course.objects.filter(id=course_id).first()
    entrol_count=StudentEntrollment.objects.filter(course=course).count()
    entrollStatus=StudentEntrollment.objects.filter(course=course,student=student,isPaid=True).count()
    print(entrol_count)
    if entrollStatus:
        return Response({'bool':True,'count':entrol_count})
    else:
        return Response({'bool':False})

class FreeEntroll(APIView):

    permission_classes=[IsAuthenticated]

    def post(self, request, format=None):
        print(request.data)
        data=request.data
        course_id=data['course']
        course_name=Course.objects.get(id=course_id).title
        student_name=Account.objects.get(id=data['student']).username
        print(student_name)
        print(course_id)
        teacher_mail=Course.objects.get(id=course_id).teacher.email
        print(teacher_mail)
        serializer = FreeOrderSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail('Hello  ',student_name+
            ' has been Entrolled '+course_name,
            'icart312@gmail.com'
            ,[teacher_mail]   
            )
            print("email sent")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
