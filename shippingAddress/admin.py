from django.contrib import admin

# Register your models here.
from .models import ShippingAddress
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display=("name","phone_number","address")

    
admin.site.register(ShippingAddress,ShippingAddressAdmin)