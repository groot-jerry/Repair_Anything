# Create your models here.

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)  # 'admin', 'user', 'technician'

    # Add other user-related fields as needed
    def __str__(self):
        return f'{self.user}- Role: {self.role}'
