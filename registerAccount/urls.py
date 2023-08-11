from django.urls import path
from.views import registerAccount_upload_view
urlpatterns=[
    path("registerAccount/upload/",registerAccount_upload_view,name="registerAccount_upload_view"),
    # path("products/list/",products_list,name="products_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
