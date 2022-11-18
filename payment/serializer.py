from rest_framework import serializers

from .models import StudentEntrollment

class OrderSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = StudentEntrollment
        fields = '__all__'
        depth = 1

class FreeOrderSerialzer(serializers.ModelSerializer):
    class Meta:
        model = StudentEntrollment
        fields = '__all__'
