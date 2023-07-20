from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("payment_details","order_status","items","customer_information")

    
admin.site.register(Order,OrderAdmin)
