from django.urls import path

from . import views

urlpatterns = [
    path('razorpay/pay/', views.start_payment, name="payment"),
    path('payment/success/', views.handle_payment_success, name="payment_success"),
    # path('payment/',views.PaymentCreate.as_view()),
    path('entroll_status/<int:student_id>/<int:course_id>/',views.fetch_entroll_status),
    path('free_entroll/',views.FreeEntroll.as_view()),
    

]