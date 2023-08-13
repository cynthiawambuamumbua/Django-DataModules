from django.urls import path
from .views import shipment_upload_view, shipment_list, shipment_detail_view,edit_shipment_view

urlpatterns = [
    path("shipment/upload/", shipment_upload_view, name="shipment_upload_view"),
    path("shipment/list/", shipment_list, name="shipment_list"),
    path("shipment/<int:id>/", shipment_detail_view, name="shipment_detail_view"), 
    path('/shipment/edit/<int:id>/',edit_shipment_view,name='edit_shipment_view')
]