from django.urls import path
from.views import category_upload_view,category_list,category_detail_view,edit_category_view
urlpatterns=[
    path("category/upload/",category_upload_view,name="category_upload_view"),
    path("category/list/",category_list,name="category_list"),
    path("category/<int:id>",category_detail_view,name="category_detail_view"),
    path('/category/edit/<int:id>/',edit_category_view,name='edit_category_view')
]
