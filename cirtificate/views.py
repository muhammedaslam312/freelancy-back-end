from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import Account
from teacher_app.models import Course
from datetime import date
# Create your views here.
from .helper import save_pdf

class GeneratePdf(APIView):
    def get(self,request,stu_id,course_id):
        student_objs = Account.objects.get(pk=stu_id)
        course = Course.objects.get(pk=course_id)
        
        print(student_objs)
        params = {
            
            'student_objs' : student_objs,
            'course' : course
        }
        file_name , status = save_pdf(params)

        if not status:
            return Response({'status': 400})
        
        return Response({'status': 200, 'path':f'/media/static/{file_name}.pdf'})