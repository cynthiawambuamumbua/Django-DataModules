from rest_framework import serializers
from customer.models import Customer
from inventory.models import Product
from category.models import Category
from basket.models import Basket

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

class BasketSerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    class Meta:
        model=Basket
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"