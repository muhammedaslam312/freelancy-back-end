from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Chapter, CourseCategory, Teacher,Course
from django.contrib.auth.hashers import make_password
from payment.models import StudentEntrollment

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields=['id','full_name','email','password','qualification','mobile_no','skills','is_active']

        extra_kwargs ={
            'password' : {'write_only': True}
        }


    def save(self):
        reg = Teacher.objects.create(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name'],
            
            mobile_no=self.validated_data['mobile_no'],
            # password=self.validated_data['password'], 
            password = make_password(self.validated_data['password']),
            qualification = self.validated_data['qualification'],
            skills = self.validated_data['skills'],

            
        )
        print(reg)
        
        return reg

class CorseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields=['id','title','description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        
        fields=['id','category','teacher','title','discription','feature_image','used_techs']
        

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields=['id','course','title','discription','video','remark']

class EntrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntrollment
        fields='__all__'
        depth = 1

class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields=['total_courses','total_chapters','total_students']

