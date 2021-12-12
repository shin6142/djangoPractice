from django.shortcuts import render
from . import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import UpdateView, DeleteView

from blog.models import Post

from . import forms
# Create your views here.


def insert_post(request):
    insert_form = forms.PostInsertForm(
        request.POST or None, request.FILES or None)
    if insert_form.is_valid():
        insert_form.save()
        insert_form = forms.PostInsertForm()
    return render(
        request, 'blog/insert_post.html', context={
            'insert_form': insert_form
        }
    )


def posts_list(request):
    posts = Post.objects.all()
    return render(
        request, 'blog/posts_list.html', context={
            'posts': posts
        }
    )
