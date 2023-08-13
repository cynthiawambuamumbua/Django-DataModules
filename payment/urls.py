from django.urls import path
from.views import payment_upload_view,payment_list,payment_detail_view,edit_payment_view
urlpatterns=[
    path("payment/upload/",payment_upload_view,name="payment_upload_view"),
    path("payment/list/",payment_list,name="payment_list"),
    path("products/<int:id>",payment_detail_view,name="payment_detail_view"),
    path('/products/edit/<int:id>/',edit_payment_view,name='edit_payment_view')
]
