from django.db import models

# Create your models here.

from django.db import models
from users.models import UserProfile
from products.models import Product


class Payment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    # Add other payment-related fields as needed

    def __str__(self):
        return f'{self.product}- Payment By: {self.user}-{self.amount}-{self.payment_date}'
