from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path("insert_post", views.insert_post, name="insert_post"),
    path("posts_list", views.posts_list, name="posts_list"),
    path("update_post/<int:id>", views.update_post, name="update_post"),
    path("delete_post/<int:id>", views.delete_post, name="delete_post"),
    path("insert_multipul_form", views.insert_multipul_posts,
         name="insert_multipul_form"),
]
