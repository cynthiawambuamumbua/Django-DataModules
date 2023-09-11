from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from .serializers import ProductSerializer
from .serializers import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from category.models import Category
from .serializers import CategorySerializer
from basket.models import Basket
from .serializers import BasketSerializer

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    def get(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        customer.delete()
        return Response("customer deleted",status=status.HTTP_204_NO_CONTENT)
    
class ProductListView(APIView):
    def get(self, request):
        products= Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        product=Product.objects.get(id=id)
        product.delete()
        return Response("product deleted",status=status.HTTP_204_NO_CONTENT)

class CategoryListView(APIView):
    def get(self, request):
        category= Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get(self,request,id,format=None):
        category=Category.objects.get(id=id)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        category=Category.objects.get(id=id)
        serializer=CategorySerializer(category,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        category=Category.objects.get(id=id)
        category.delete()
        return Response("category deleted",status=status.HTTP_204_NO_CONTENT)
    
class AddToCartView(APIView):
    def post(self, request,format=None):
        cart_id=request.data["cart_id"]
        product_id=request.data["product_id"]
        cart=Basket.objects.get(id=cart_id)
        product=Product.objects.get(id=product_id)
        update_cart=cart.add_product(product)
        serializer=BasketSerializer(update_cart)
        return Response(serializer.data)
        

# class BasketDetailView(APIView):
#     def get(self,request,id,format=None):
#         basket=Basket.objects.get(id=id)
#         serializer=BasketSerializer(basket)
#         return Response(serializer.data)
    
#     def put(self,request,id,format=None):
#         basket=Basket.objects.get(id=id)
#         serializer=BasketSerializer(basket,request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id,format=None):
#         basket=Basket.objects.get(id=id)
#         basket.delete()
#         return Response("basket deleted",status=status.HTTP_204_NO_CONTENT)
    

    
