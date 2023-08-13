from django.contrib import admin

# Register your models here.
from .models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display=("name","description","date_created")
  
admin.site.register(Shipment,ShipmentAdmin)

