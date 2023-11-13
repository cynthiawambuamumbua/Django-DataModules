from django.urls import path
from.views import registerAccount_upload_view,registerAccount_list,edit_registerAccount_view,registerAccount_detail_view
urlpatterns=[
    path("registerAccount/upload/",registerAccount_upload_view,name="registerAccount_upload_view"),
    path("registerAccount/list/",registerAccount_list,name="registerAccount_list"),
    path("registerAccount/<int:id>",registerAccount_detail_view,name="registerAccount_detail_view"),
    path('registerAccount/edit/<int:id>/',edit_registerAccount_view,name='edit_registerAccount_view')
]
