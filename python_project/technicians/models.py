from django.db import models

# Create your models here.

from django.db import models
from users.models import UserProfile


class Technician(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255)
    # Add other technician-related fields as needed

    def __str__(self):
        return f'{self.user}- Skill: {self.skills}'