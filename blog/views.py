from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.exceptions import PermissionDenied

from blog.models import Post

from . import forms
# Create your views here.


class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    model = Post
    context_object_name = "post"

    def get_object(self):
        post = super().get_object()
        if post.is_published:
            return post
        else:
            raise PermissionDenied


class PostCreateView(CreateView):

    model = Post
    form_class = forms.PostCreateFrom
    success_url = reverse_lazy('')
