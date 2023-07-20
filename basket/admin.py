from django.contrib import admin

# Register your models here.
from .models import Basket
class BasketAdmin(admin.ModelAdmin):
    list_display=("name","quantity","price","total_price")
admin.site.register(Basket,BasketAdmin)