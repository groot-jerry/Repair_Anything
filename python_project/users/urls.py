

from django.urls import path

from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView, name='user_registration'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    # Add other user-related URLs as needed
]
