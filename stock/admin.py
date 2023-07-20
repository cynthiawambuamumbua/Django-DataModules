from django.contrib import admin

# Register your models here.
from .models import Stock
class StockAdmin(admin.ModelAdmin):
    list_display=("name","price","image","quantity","description","date_created","date_updated")
    
admin.site.register(Stock,StockAdmin)