from django.urls import path
from .views import TechnicianAssignmentView, TechnicianRegistrationView


urlpatterns = [
    path('register/', TechnicianRegistrationView, name='register_technician'),
    path('technicians/', TechnicianAssignmentView.as_view(), name='assign_technician')
    # Add other technician-related URLs as needed
]
