from django.db import models

# Create your models here.
class Basket(models.Model):
  name=models.CharField(max_length=32)
  price =models.DecimalField(max_digits=8, decimal_places=2)
  image=models.ImageField()
  total_price=models.DecimalField(max_digits=8,decimal_places=2)
  quantity=models.IntegerField()
  def __str__(self):
        return self.name