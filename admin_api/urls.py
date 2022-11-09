from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
        #userpanel
        path('blockuser/<int:id>/',views.BlockUser.as_view(),name='blockuser'),
        path('unblockuser/<int:id>/',views.UnblockUser.as_view(),name='unblockuser'),
        path('getusers/',views.GetUsersView.as_view(),name='getusers'),

        #teacherpanel
       
        path('verifyteacher/<int:id>/',views.VerifyTeacher.as_view(),name='verifyteacher'),
        path('getteachers/',views.GetTeachersView.as_view(),name='getusers'),
        path('admin/course_category_list/',views.CourseCategoryDetail.as_view(),name='getcategory'),
        
]
