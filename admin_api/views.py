
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated


from main.models import Account
from main.serializers import AccountSerializer
from .serializer import UpdateTeacherSerializer, UpdateUserSerializer,CourseSerializer,StudentEntrollmentSerializer,CaroselSerializer,EntrollSeializer
from payment.models import StudentEntrollment
from .models import Carosel

from rest_framework.response import Response

from teacher_app.models import CourseCategory, Teacher,Course
from teacher_app.serializers import CorseCategorySerializer, TeacherSerializer
from rest_framework import generics

from rest_framework import status
from django.core.mail import send_mail
from rest_framework import permissions

from django.db.models import Avg, Count, Min, Sum





# Create your views here.

class GetUsersView(APIView):
    permission_classes=[IsAdminUser]
    # authentication_classes=[IsAuthenticated]


    def get(self,request):
        Accounts = Account.objects.all().exclude(is_superuser=True)
        serializer = AccountSerializer(Accounts,many=True)
        return Response (serializer.data)

class BlockUser(APIView):
    #permission_classes=[IsAdminUser]
    # authentication_classes=[IsAuthenticated]
    
    print("aaaa")
    def patch(self,request,id):
        details = Account.objects.get(id=id)
        if details.is_active:
            details.is_active = False
        else:
            details.is_active = True
        serializer = UpdateUserSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("user blocked")
            return Response(serializer.data)
        else:
            print('vendor action failed')
            print(serializer.errors)
            return Response(serializer.errors)    

class UnblockUser(APIView):
    permission_classes=[IsAdminUser]
    
    def patch(self,request,id):
        details = Account.objects.get(id=id)
        if details.is_active == False:
            details.is_active = True
        serializer = UpdateUserSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("user unblocked")
            return Response(serializer.data)
        else:
            print('vendor action failed')
            print(serializer.errors)
            return Response(serializer.errors)    


class GetTeachersView(APIView):
    #authentication_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]


    def get(self,request):
        Accounts = Teacher.objects.all()
        serializer = TeacherSerializer(Accounts,many=True)
        return Response (serializer.data)




class VerifyTeacher(APIView):
    # permission_classes=[IsAdminUser]
    
    def patch(self,request,id):
        details = Teacher.objects.get(id=id)
        print(details.id)
        if details.is_active == False:
            details.is_active = True

            mail=details.email
            send_mail('Hello  ',
            'Congratulations, your Teacher application is approved.',
            'icart312@gmail.com'
            ,[mail]   
            ,fail_silently=False)
            print("email sent")

        else:
            details.is_active= False
        serializer = UpdateTeacherSerializer(details,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            print("teacher verified")
            return Response(serializer.data)
        else:
            print('teacher action failed')
            print(serializer.errors)
            return Response(serializer.errors)    

class CourseCategoryDetail(generics.ListCreateAPIView):
    
    permission_classes=[IsAdminUser]
    queryset = CourseCategory.objects.all()
    serializer_class = CorseCategorySerializer

class CourseCategoryDelete(APIView):
    permission_classes=[IsAdminUser]
    def delete(self, request, pk):
        category = CourseCategory.objects.get(id=pk)
        category.delete()
        response={'message':"category deleted"}
        return Response(response,status=status.HTTP_204_NO_CONTENT) 
    
class GetAllCourses(generics.ListAPIView):
    
    permission_classes=[IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class GetEntrolledDetails(generics.ListAPIView):
    
    permission_classes=[IsAdminUser]
    queryset = StudentEntrollment.objects.all()
    serializer_class = StudentEntrollmentSerializer

class AddCarosel(APIView):
    # authentication_classes=[IsAuthenticated]
    permission_classes=[IsAdminUser]
    
    
    def post(self,request):
        try:
            serializer = CaroselSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(serializer.errors)
        except:
            message = {'detail':'somthing whent worng'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        carosel = Carosel.objects.get(id=pk)
        carosel.delete()
        response={'message':"carosel deleted"}
        return Response(response,status=status.HTTP_204_NO_CONTENT) 
    
    def patch(self, request,id):
        try:

            details = Carosel.objects.get(id=id)
            serializer = CaroselSerializer(details,data=request.data,partial = True)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                print("Update Carosel successfully updated")
                return Response(serializer.data)
            else:
                print("Update Carosel failed")
                print(serializer.errors)
                return Response(serializer.errors)
        except:
            message = {'detail':'somthing whent worng'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

class GetAllCarosel(APIView):
    # authentication_classes=[IsAuthenticated]

    def get(self,request):
        print("//////")
        
        courses = Carosel.objects.all()
        serializer = CaroselSerializer(courses,many=True)
        
        return Response (serializer.data)

class GetEntrolledDetails(APIView):
    permission_classes=[IsAdminUser]
      
    def get(self,request):
        print("//////")
        
        student_entroll = StudentEntrollment.objects.all()
        serializer = EntrollSeializer(student_entroll,many=True)
        # total_price = StudentEntrollment.objects.aggregate(Sum('order_amount'))
        # print(total_price)
        return Response (serializer.data)

class AdminCommision(APIView):
    permission_classes=[IsAdminUser]

    def get(self,request):
        Entrolled_course=StudentEntrollment.objects.all()
        total_earned=0
        admin_commision=0
        for i in Entrolled_course:
            amount=int(i.order_amount)
            print('====================')
            print(amount)
            print(type(amount))
            print(type(total_earned),'--------------')
            total_earned+=amount
            admin_commision += amount*10/100
        response={'total_earned':total_earned,'admin_commision':admin_commision}
        return Response(response) 

       


            
       








