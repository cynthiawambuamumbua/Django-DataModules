from django.urls import path
from.views import stock_upload_view,stock_detail_view,stock_list,edit_stock_view
urlpatterns=[
    path("stock/upload/",stock_upload_view,name="stock_upload_view"),
    path("stock/list/",stock_list,name="stock_list"),
    path("stock/<int:id>",stock_detail_view,name="stock_detail_view"),
    path('/stock/edit/<int:id>/',edit_stock_view,name='edit_stock_view')
]
