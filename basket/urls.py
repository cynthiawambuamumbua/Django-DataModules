from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('detail/<int:basket_id>/', views.basket_detail, name='detail'),
]