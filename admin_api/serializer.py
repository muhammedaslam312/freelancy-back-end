from rest_framework import serializers
from main.models import Account
from teacher_app.models import Teacher,Course
from payment.models import StudentEntrollment
from .models import Carosel

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields='__all__'
        extra_kwargs ={
            'password' : {'write_only': True}
        }

class UpdateTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields='__all__'
        extra_kwargs ={
            'password' : {'write_only': True}
        }

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields='__all__'

class StudentEntrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntrollment
        fields='__all__'

class CaroselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carosel
        fields='__all__'


class EntrollSeializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.email')
    course = serializers.CharField(source='course.title')
    teacher = serializers.CharField(source='course.teacher')
    
    class Meta:
        model = StudentEntrollment
        fields = ('id', 'student', 'course','teacher','order_amount','admin_commition')