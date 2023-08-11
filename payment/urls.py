from django.urls import path
from.views import payment_upload_view,payment_list
urlpatterns=[
    path("payment/upload/",payment_upload_view,name="payment_upload_view"),
    path("payment/list/",payment_list,name="payment_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
