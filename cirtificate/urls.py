from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

urlpatterns = [
    path('pdf/<int:stu_id>/<int:course_id>/' , views.GeneratePdf.as_view())
]