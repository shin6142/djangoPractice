from django.urls import path
from blog.views import PostList, PostDetail, PostCreateView

urlpatterns = [
    path("", PostList.as_view(), name=""),
    path("post/<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("post_create", PostCreateView.as_view(), name="post_create"),
]
