from django.db import models

# Create your models here.
class Order(models.Model):
    payment_details=models.CharField(max_length=32)
    order_status=models.CharField(max_length=32)
    items=models.CharField(max_length=32)
    customer_information=models.CharField(max_length=32)
    def __str__(self):
        return self.payment_details
