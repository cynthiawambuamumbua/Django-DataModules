from django.urls import path
from.views import order_upload_view,order_list,order_detail_view,edit_order_view
urlpatterns=[
    path("order/upload/",order_upload_view,name="order_upload_view"),
    path("order/list/",order_list,name="order_list"),
    path("order/<int:id>",order_detail_view,name="order_detail_view"),
    path('order/edit/<int:id>/',edit_order_view,name='edit_order_view')
]
