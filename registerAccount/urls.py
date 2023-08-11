from django.urls import path
from.views import registerAccount_upload_view,registerAccount_list
urlpatterns=[
    path("registerAccount/upload/",registerAccount_upload_view,name="registerAccount_upload_view"),
    path("registerAccount/list/",registerAccount_list,name="registerAccount_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
