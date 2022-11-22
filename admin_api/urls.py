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
        path('blockteacher/<int:id>/',views.VerifyTeacher.as_view(),name='verifyteacher'),
        path('getteachers/',views.GetTeachersView.as_view(),name='getusers'),

        path('admin/categorylist/',views.CourseCategoryDetail.as_view(),name='getcategory'),
        path('admin/addcategory/',views.CourseCategoryDetail.as_view(),name='addcategory'),
        path('admin/deletecategory/<int:pk>/',views.CourseCategoryDelete.as_view(),name='deletecategory'),

        path('getallcourse/',views.GetAllCourses.as_view()),
        path('getentrolled/',views.GetEntrolledDetails.as_view(),name='admingetentroll'),

         path('allcarosel/',views.GetAllCarosel.as_view(),name='addcarosel'),
        path('addcarosel/',views.AddCarosel.as_view(),name='addcarosel'),
        path('deletecarosel/<int:pk>/',views.AddCarosel.as_view(),name='deletecarosel'),
        

        

        
]
