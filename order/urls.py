from django.urls import path
from.views import order_upload_view,order_list
urlpatterns=[
    path("order/upload/",order_upload_view,name="order_upload_view"),
    path("order/list/",order_list,name="order_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
