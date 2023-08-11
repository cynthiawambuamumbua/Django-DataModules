from django.urls import path
from.views import customer_upload_view,customer_list
urlpatterns=[
    path("customer/upload/",customer_upload_view,name="customer_upload_view"),
    path("customer/list/",customer_list,name="customer_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
