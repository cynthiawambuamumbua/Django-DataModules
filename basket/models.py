from django.db import models

# Create your models here.
class Basket(models.Model):
  # name=models.CharField(max_length=32)
  # price =models.DecimalField(max_digits=8, decimal_places=2)
  # image=models.ImageField()
  # total_price=models.DecimalField(max_digits=8,decimal_places=2)
  # quantity=models.IntegerField()
  products=models.ManyToManyField()
  # def __str__(self):
  #       return self.name
  def add_product(self,product):
      self.product.add(product)
      self.save()
      return self
  def get_total(self):
     products=self.products
     total=0
     for product in products:
        total+=product.price
        return total
     # Remove the product from the basket
  # Remove the product from the basket

     
    #  the shorter method to do it
    #  total=sum([product.price for product in self.products])
