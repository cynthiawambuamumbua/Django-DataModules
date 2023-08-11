from django.urls import path
from.views import reviews_upload_view,reviews_list
urlpatterns=[
    path("reviews/upload/",reviews_upload_view,name="reviews_upload_view"),
    path("reviews/list/",reviews_list,name="reviews_list"),
    # path("products/<int:id>",product_detail_view,name="product_detail_view"),
    # path('/products/edit/int:id>/',edit_product_view,name='edit_product_view')
]
