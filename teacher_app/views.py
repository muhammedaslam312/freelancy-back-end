from os import access
from tabnanny import check
from urllib import response
from venv import create
from rest_framework.views import APIView
from rest_framework.response import Response

from .authentication import JWTTeacherAuthentication, create_access_token, create_refresh_token

from rest_framework import status

import datetime

from .serializers import ChapterSerializer, CorseCategorySerializer, CourseSerializer, TeacherSerializer,EntrollmentSerializer,TeacherDashboardSerializer,EntrollSeializer

from .models import Chapter, Teacher, TeacherToken,CourseCategory,Course
from rest_framework import generics,permissions

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from payment.models import StudentEntrollment

from django.contrib.auth.hashers import check_password

import jwt

# Create your tests here.

class LoginTeacherAPIView(APIView):
    def post(self,request):
        email = request.data['email']
        givenpassword = request.data['password']
        print('*****')
        print(givenpassword)

        teacher = Teacher.objects.filter(email=email).first()
        print(teacher)

        if teacher is None:
            response = Response()

            response.data={
                'message': 'Invalid email'
            }
            return response

        storedpassword =str(teacher.password)

        ans = check_password(givenpassword,storedpassword)
        print(ans)

        if not check_password(givenpassword,storedpassword):
            response=Response()
            response.data = {
                'message':'password Incorrect'
            }
            return response
        

        print('*11111111***')
        print(teacher.is_active)
        if teacher.is_active:
            print("**22222222222***")
            access_token =create_access_token(teacher.id,teacher.full_name,teacher.is_active)
            refresh_token = create_refresh_token(teacher.id)
            print("**333333333****")
            print(access_token)

            TeacherToken.objects.create(
                teacher_id = teacher.id,
                token = refresh_token,
                expired_at =  datetime.datetime.utcnow()+datetime.timedelta(seconds=7)

            )

            response = Response()

            response.set_cookie(key='refresh_token',value=refresh_token,httponly=True)
            response.data = {
                'token':access_token,
                'refresh':refresh_token,
                # 'user_id':teacher.id,
                # 'first_name':teacher.full_name,
                # 'email':teacher.email,
                # 'mobile':teacher.mobile_no,
                # 'is_active':teacher.is_active,
                

            }
            
            return response
       
        else:
            response=Response()
            response.data ={
                'message':'Not verified Teacher'
            }
            return response
   

class TeacherList(generics.ListCreateAPIView):
    #list all teachers
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    

class TecherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class=TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]

class GetAllCategories(generics.ListCreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CorseCategorySerializer
    authentication_classes = [JWTTeacherAuthentication]
    
   

class CourseCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CorseCategorySerializer
    authentication_classes = [JWTTeacherAuthentication]
    
class CreateCourse(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes=  [JWTTeacherAuthentication]
    

class GetAllTeacherCourses(APIView):
    authentication_classes=  [JWTTeacherAuthentication]
    
    def get(self,request,id):
        print("//////")
        # teacher = Teacher.objects.filter(id=id)

        # print(teacher)
        Accounts = Course.objects.filter(teacher=id)
        serializer = CourseSerializer(Accounts,many=True)
        
        return Response (serializer.data)

class CreateChapter(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    authentication_classes=  [JWTTeacherAuthentication]

class GetAllChapters(APIView):
    authentication_classes=[JWTTeacherAuthentication]

    def get(self,request,id):
        chapters =Chapter.objects.filter(course=id)
        serializer = ChapterSerializer(chapters,many=True)
        return Response(serializer.data)

class DeleteChapter(APIView):
    authentication_classes=[JWTTeacherAuthentication]

    def delete(self, request, pk):
        chapter = Chapter.objects.get(id=pk)
        chapter.delete()
        response={'message':"chapter deleted"}
        return Response(response,status=status.HTTP_204_NO_CONTENT) 
    

class GetEntrolledStudents(APIView):
    authentication_classes=[JWTTeacherAuthentication]

    def get(self,request,id):
        # course=Course.objects.filter(teacher=id)
        # serializer_list=[]
        # for i in course:
        #     entrollment =StudentEntrollment.objects.filter(course__teacher=i.id)
        #     if entrollment:
        #         serializer = EntrollmentSerializer(entrollment,many=True)
        #         serializer_list.append(serializer.data)
        entrollment =StudentEntrollment.objects.filter(course__teacher=id)
        serializer = EntrollmentSerializer(entrollment,many=True)
        return Response(serializer.data)

class GetTeacherDashboard(APIView):
     authentication_classes=[JWTTeacherAuthentication]
     def get(self,request,id):
        total_courses=Course.objects.filter(teacher=id).count()
        total_chapters=Chapter.objects.filter(course__teacher=id).count()
        total_students=StudentEntrollment.objects.filter(course__teacher=id).count()
        
        data = {
            'total_courses':total_courses,
            'total_chapters':total_chapters,
            'total_students':total_students
        }
        return Response(data)

class GetTransactionDetails(APIView):
    authentication_classes=[JWTTeacherAuthentication]
      
    def get(self,request,id):
        print("//////")
        
        teacher = Teacher.objects.get(pk=id)
        student_entroll = StudentEntrollment.objects.filter(course__teacher=teacher)
        serializer = EntrollSeializer(student_entroll,many=True)
        # total_price = StudentEntrollment.objects.aggregate(Sum('order_amount'))
        # print(total_price)
        return Response (serializer.data)

class TeacherCommision(APIView):
    authentication_classes=[JWTTeacherAuthentication]

    def get(self,request,id):
        Entrolled_course=StudentEntrollment.objects.filter(course__teacher=id)
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

