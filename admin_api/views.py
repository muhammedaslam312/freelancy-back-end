from functools import partial
import imp
from msilib.schema import Class
from re import U
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated


from main.models import Account
from main.serializers import AccountSerializer
from .serializer import UpdateTeacherSerializer, UpdateUserSerializer

from rest_framework.response import Response

from teacher_app.models import CourseCategory, Teacher
from teacher_app.serializers import CorseCategorySerializer, TeacherSerializer
from rest_framework import generics

from django.core.mail import send_mail





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
    





