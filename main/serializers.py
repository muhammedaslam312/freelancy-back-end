from dataclasses import fields
import email
import imp
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User

from teacher_app.models import Course
from . import models
from payment.models import StudentEntrollment


class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Account
        fields=['id','email', 'username','password','bio','mobile','courses_entrolled','interests','profile_dp','is_active','is_superuser','last_login','joined_date']

        extra_kwargs ={
            'password' : {'write_only': True}
        }

    def validate_password(self,value):
        if len(value)<4:
            raise serializers.ValidationError("Password must be minimum 4 characters")
        else:
            return value

    def save(self):
        reg = models.Account(
            email=self.validated_data['email'],
            username = self.validated_data['username'],
            mobile = self.validated_data['mobile'],
            interests = self.validated_data['interests'],
            

        )           
        password = self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg

class VerifyOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ['is_active']

class SingleCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Course
        fields=['id','category','teacher','title','discription','feature_image','used_techs','course_chapters','price','related_courses']
        depth = 1

class RecomentedCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Course
        fields=['id','category','teacher','title','discription','feature_image','used_techs','price','course_chapters']
        
class CourseRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model =models.CourseRating
        fields='__all__'

class EntrolledCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntrollment
        fields=['id','course','student','order_amount','get_chapters']
        depth = 2

class FavoriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteCourse
        fields='__all__'

class GetFavoriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FavoriteCourse
        fields='__all__'  
        depth = 1     
        
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentAssignment
        fields = '__all__'
        

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class AssignmentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssignmentAnswer
        fields = '__all__'
        
class AssignmentAnswerTeacherSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='assignment.title')
    class Meta:
        model = models.AssignmentAnswer
        fields = ('title','detail','file')
