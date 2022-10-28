from dataclasses import fields
import email
import imp
from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


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
            mobile = self.validated_data['mobile']
        )           
        password = self.validated_data['password']
        reg.set_password(password)
        reg.save()
        return reg