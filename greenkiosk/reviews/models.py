from django.db import models

# Create your models here.
class Reviews(models.Model):
    name=models.CharField(max_length=32)
    comments=models.CharField(max_length=32)
   

