from django.urls import path
from.views import shippingAddress_upload_view,shippingAddress_detail_view,shippingAddress_list,edit_shippingAddress_view
urlpatterns=[
    path("shippingAddress/upload/",shippingAddress_upload_view,name="shippingAddress_upload_view"),
    path("shippingAddress/list/",shippingAddress_list,name="shippingAddress_list"),
    path("shippingAddress/<int:id>",shippingAddress_detail_view,name="shippingAddress_detail_view"),
    path('/shippingAddress/edit/<int:id>/',edit_shippingAddress_view,name='edit_shippingAddress_view')
]
