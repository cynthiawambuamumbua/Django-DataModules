from django.contrib import admin
from .models import Basket

class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_total', 'product_count')

    def get_total(self, obj):
        return obj.get_total()

    def product_count(self, obj):
        return obj.products.count()

    get_total.short_description = 'Total'
    product_count.short_description = 'Product Count'

admin.site.register(Basket, BasketAdmin)
