from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Shipment(models.Model):
    name=models.CharField(max_length=32)
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
