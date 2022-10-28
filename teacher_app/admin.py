
from pyexpat import model
from django.contrib import admin

from . import models


from .models import Chapter, Teacher,CourseCategory,Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    model = models.Course
    list_display = ('id', 'title') 

admin.site.register(Teacher)
admin.site.register(CourseCategory)
admin.site.register(Course,CourseAdmin)
admin.site.register(Chapter)





        
