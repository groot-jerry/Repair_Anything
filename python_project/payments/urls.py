from django.urls import path
from .views import PaymentView

urlpatterns = [
    path('payment/<int:product_id>/', PaymentView.as_view(), name='payment'),
    # Add other payment-related URLs as needed
]
