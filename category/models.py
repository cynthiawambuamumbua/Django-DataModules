from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=32)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image=models.ImageField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
