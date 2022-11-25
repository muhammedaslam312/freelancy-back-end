from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

urlpatterns = [
    path('teacher-token/',views.LoginTeacherAPIView.as_view(),name='loginteacher'),

    path('teacher/',views.TeacherList.as_view()),
    path('teacher/<int:pk>/',views.TecherDetail.as_view()),
    path('course_category_list/',views.GetAllCategories.as_view()),
    path('course_category_details/<int:pk>/',views.CourseCategoryDetail.as_view()),
    path('create_course/',views.CreateCourse.as_view()),
    path('get_courses/<int:id>/',views.GetAllTeacherCourses.as_view()),

    path('get_chapters/<int:id>/',views.GetAllChapters.as_view()),
    path('create_chapter/',views.CreateChapter.as_view()),
    path('delete_chapter/<int:pk>/',views.DeleteChapter.as_view()),
    path('entrolled_student/<int:id>/',views.GetEntrolledStudents.as_view()),
    path('teacher_dashboard/<int:id>/',views.GetTeacherDashboard.as_view()),

    path('teacher/getentrolled/<int:id>/',views.GetTransactionDetails.as_view(),name='teachergetentroll'),
    path('teachercommition/<int:id>/',views.TeacherCommision.as_view()),

    



]