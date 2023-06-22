from typing import Any
from django.db import models

# Create your models here.
class ShippingAddress(models.Model):
    name=models.CharField(max_length=32)
    phone_number=models.CharField(max_length=10)
    address=models.CharField(max_length=32)
    def __str__(self):
        return self.name
