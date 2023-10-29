from django.shortcuts import render
from users.models import UserProfile
from technicians.models import Technician


def home(request):
    technicians = Technician.objects.all()
    users = UserProfile.objects.all()
    return render(request, 'home.html', {"users": users})
