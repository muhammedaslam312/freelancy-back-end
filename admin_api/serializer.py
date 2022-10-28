from rest_framework import serializers
from main.models import Account
from teacher_app.models import Teacher

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
