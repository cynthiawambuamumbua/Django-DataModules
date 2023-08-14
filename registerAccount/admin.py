from django.contrib import admin

# Register your models here.
from .models import RegisterAccount
class RegisterAccountAdmin(admin.ModelAdmin):
    list_display=("first_name","second_name","email","phone_number","password","address")
    
admin.site.register(RegisterAccount,RegisterAccountAdmin)
