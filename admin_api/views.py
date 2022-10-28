from functools import partial
from msilib.schema import Class
from re import U
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from main import serializers

from main.models import Account
from main.serializers import AccountSerializer
from .serializer import UpdateTeacherSerializer, UpdateUserSerializer

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from teacher_app.models import Teacher
from teacher_app.serializers import TeacherSerializer




# Create your views here.

class GetUsersView(APIView):
    # permission_classes=[IsAdminUser]


    def get(self,request):
        Accounts = Account.objects.all().exclude(id=1)
        serializer = AccountSerializer(Accounts,many=True)
        return Response (serializer.data)

class BlockUser(APIView):
    #permission_classes=[IsAdminUser]
    
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
    # permission_classes=[IsAdminUser]
    
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
    # permission_classes=[IsAdminUser]


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



