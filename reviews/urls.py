from django.urls import path
from.views import reviews_upload_view,reviews_list,reviews_detail_view,edit_reviews_view
urlpatterns=[
    path("reviews/upload/",reviews_upload_view,name="reviews_upload_view"),
    path("reviews/list/",reviews_list,name="reviews_list"),
    path("reviews/<int:id>",reviews_detail_view,name="reviews_detail_view"),
    path('/reviews/edit/<int:id>/',edit_reviews_view,name='edit_reviews_view')
]
