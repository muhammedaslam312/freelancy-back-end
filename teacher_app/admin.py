
from pyexpat import model
from django.contrib import admin

from . import models


from .models import Chapter, Teacher,CourseCategory,Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    model = models.Course
    list_display = ('id', 'title') 

class TeacherAdmin(admin.ModelAdmin):
    model = models.Teacher
    list_display = ('id', 'email','qualification') 

admin.site.register(Teacher,TeacherAdmin)
admin.site.register(CourseCategory)
admin.site.register(Course,CourseAdmin)
admin.site.register(Chapter)





        
