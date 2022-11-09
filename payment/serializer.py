from rest_framework import serializers

from .models import StudentEntrollment

class OrderSerializer(serializers.ModelSerializer):
    order_date = serializers.DateTimeField(format="%d %B %Y %I:%M %p")

    class Meta:
        model = StudentEntrollment
        fields = '__all__'
        depth = 1