from django.db import models

# Create your models here.
class Stock(models.Model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    quantity=models.IntegerField()
    image=models.ImageField()
    description=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
