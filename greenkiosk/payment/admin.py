from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("name","payment_method","payment_status","expiration_date")

    
admin.site.register(Payment,PaymentAdmin)

