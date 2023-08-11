from django.urls import path
from.views import stock_upload_view
urlpatterns=[
    path("stock/upload/",stock_upload_view,name="stock_upload_view"),
    # path("products/list/",products_list,name="products_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
