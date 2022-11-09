from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

urlpatterns = [
    #login
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/',views.RegisterAccount.as_view()),
    path('user/verify/',views.VerifyUserOtp.as_view()),
    path('get_allcourses/latest/',views.GetAllCourses.as_view()),
    path('recomented_courses/<int:id>/',views.RecomentedCourses.as_view()),
    path('course_details/<int:id>/',views.CourseDetails.as_view()),
    path('user/get_chapters/<int:student_id>/<int:course_id>/',views.GetAllChapters.as_view()),
    path('post_rating/',views.PostRating.as_view()),

    #dashboard
    path('get_entrolled/<int:id>/',views.GetUserEntrolledCourses.as_view()),
    path('add_favorite/',views.StudentFavoriteCourse.as_view()),
    path('remove_favorite/<int:student_id>/<int:course_id>',views.remove_favorite_course.as_view()),
    #payment
   
    
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
