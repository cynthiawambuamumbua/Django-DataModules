from django.urls import path
from .views import shipment_upload_view, shipment_list, shipment_detail_view

urlpatterns = [
    path("shipment/upload/", shipment_upload_view, name="shipment_upload_view"),
    path("shipment/list/", shipment_list, name="shipment_list"),
    path("shipment/<int:id>/", shipment_detail_view, name="shipment_detail_view"), 
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]