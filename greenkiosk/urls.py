"""
URL configuration for greenkiosk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventory/", include ("inventory.urls")),
    path("vendor/", include ("vendor.urls")),
    path("stock/", include ("stock.urls")),
    path("shippingAddress/", include ("shippingAddress.urls")),
    path("shipment/", include ("shipment.urls")),
    path("reviews/", include ("reviews.urls")),
    path("registerAccount/", include ("registerAccount.urls")),
    path("payment/", include ("payment.urls")),
    path("order/", include ("order.urls")),
    path("customer/", include ("customer.urls")),
    path("category/", include ("category.urls")),
]
