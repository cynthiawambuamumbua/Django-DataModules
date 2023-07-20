from django.db import models

# Create your models here.
class Payment(models.Model):
    name=models.CharField(max_length=32)
    payment_method=models.CharField(max_length=12)
    payment_status=models.CharField(max_length=19)
    expiration_date=models.IntegerField()
    def __str__(self):
        return self.name
