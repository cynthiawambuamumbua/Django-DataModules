from django.contrib import admin

# Register your models here.
from .models import Inventory
class InventoryAdmin(admin.ModelAdmin):
    list_display=("name","price","image","description","date_created","date_updated")

    
admin.site.register(Inventory,InventoryAdmin)














