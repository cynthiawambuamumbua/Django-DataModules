from django.contrib import admin

# Register your models here.
from .models import Customer
class ProductsAdmin(admin.ModelAdmin):
    list_display=("name","phone_number")
admin.site.register(Customer,ProductsAdmin)
