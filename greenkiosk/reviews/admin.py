from django.contrib import admin

# Register your models here.
from .models import Reviews
class ReviewAdmin(admin.ModelAdmin):
    list_display=("name","comments")
  
admin.site.register(Reviews,ReviewAdmin)

