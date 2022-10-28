
from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pyexpat import model
from tkinter.tix import Balloon, Tree
from turtle import title
from django.db import models

# Create your models here.

class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=20)
    skills=models.TextField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '1. Teachers'

    REQUIRED_FIELDS =['password']
    def __str__(self):
        return self.email


class TeacherToken(models.Model):
    teacher_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return str(self.teacher_id) +' '+ self.token

class CourseCategory(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = '2. Course Category'


#course model
class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    feature_image = models.ImageField(upload_to='photos/course_image/',blank=True)
    title = models.CharField(max_length=150)
    discription = models.TextField()    
    used_techs = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '3. Course'

class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title =models.CharField(max_length=150)
    discription = models.TextField()
    video = models.FileField(upload_to='videos/chapter_videos/',blank=True)
    remark = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = '4. Chapters'
    def __str__(self):
        return self.title