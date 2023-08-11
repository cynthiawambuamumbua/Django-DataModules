from django.urls import path
from.views import category_upload_view,category_list
urlpatterns=[
    path("category/upload/",category_upload_view,name="category_upload_view"),
    path("category/list/",category_list,name="category_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
