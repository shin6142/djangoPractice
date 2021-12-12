from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path("insert_post", views.insert_post, name="insert_post"),
    path("posts_list", views.posts_list, name="posts_list"),
]
