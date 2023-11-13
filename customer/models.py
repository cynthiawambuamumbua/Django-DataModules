from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=32)
    phone_number=models.DecimalField(max_digits=12,decimal_places=2)
    details=models.TextField()
    def __str__(self):
        return self.name