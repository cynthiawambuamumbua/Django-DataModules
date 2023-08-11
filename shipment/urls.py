from django.urls import path
from.views import shipment_upload_view,shipment_list
urlpatterns=[
    path("shipment/upload/",shipment_upload_view,name="shipment_upload_view"),
    path("shipment/list/",shipment_list,name="shipment_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
