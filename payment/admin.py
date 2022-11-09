from django.contrib import admin

# Register your models here.


from .models import StudentEntrollment

class StudentEntrollmentAdmin(admin.ModelAdmin):
    model = StudentEntrollment
    list_display = ('student','course','isPaid','entrolled_time') 

admin.site.register(StudentEntrollment,StudentEntrollmentAdmin)

