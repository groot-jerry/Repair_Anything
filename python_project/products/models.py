
# Create your models here.
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE)
    technician = models.ForeignKey('technicians.Technician', null=True, blank=True, on_delete=models.SET_NULL)
    # Add other product-related fields as needed

    def __str__(self):
        return f'{self.name} of  {self.user} will Repair by: {self.technician}'