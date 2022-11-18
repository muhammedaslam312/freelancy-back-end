from django.db import models
from teacher_app.models import Course
from main.models import Account
from django.core import serializers
from teacher_app.models import Chapter
# Create your models here.

class StudentEntrollment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='entrolled_courses')
    order_amount=models.CharField(max_length=25,blank=True)
    order_payment_id =models.CharField(max_length=100,blank=True)
    student = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='entrolled_student')
    order_date  =models.DateTimeField(auto_now=True)
    isPaid = models.BooleanField(default=False)

    def __str__(self):
        return self.order_payment_id
    
    def get_chapters(self):
        get_chapters=Chapter.objects.filter(id=self.course_id)
        return serializers.serialize('json',get_chapters)
