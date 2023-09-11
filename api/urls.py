from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from .views import ProductDetailView
from .views import ProductListView
from .views import CategoryDetailView
from .views import CategoryListView
from .views import AddToCartView

urlpatterns = [
    path("customers/", CustomerListView.as_view(), name="customer_list_view"),
    path("customers/<int:id>/",CustomerDetailView.as_view(), name="customer_detail_view"),
    path("products/", ProductListView.as_view(), name="products_list_view"),
    path("products/<int:id>/",ProductDetailView.as_view(), name="product_detail_view"),
    path("category/", CategoryListView.as_view(), name="category_list_view"),
    path("category/<int:id>/",CategoryDetailView.as_view(), name="category_detail_view"),
    path("basket/", AddToCartView.as_view(), name="add_to_cart"),
]
