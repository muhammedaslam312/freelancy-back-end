from django.urls import path

from . import views

urlpatterns = [
    # path('pay/', start_payment, name="payment"),
    # path('payment/success/', handle_payment_success, name="payment_success")
    # path('payment/',views.PaymentCreate.as_view()),
    path('entroll_status/<int:student_id>/<int:course_id>/',views.fetch_entroll_status),
    

]