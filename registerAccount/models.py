from django.db import models

# Create your models here.
class RegisterAccount(models.Model):
    first_name=models.CharField(max_length=32)
    second_name=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    password=models.CharField(max_length=32)
    phone_number=models.CharField(max_length=32)
    address=models.CharField(max_length=32)
    
    def __str__(self):
        return self.first_name
    def __str__(self):
        return self.second_name
    
