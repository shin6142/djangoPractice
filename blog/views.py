from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from blog.models import Post
from . import forms
from django.forms import modelformset_factory

import os
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


def update_post(request, id):
    post = Post.objects.get(id=id)
    update_form = forms.PostUpdateForm(
        initial={
            'title': post.title,
            'content': post.content,
            'is_published': post.is_published,
            'image': post.image,
        }
    )
    if request.method == 'POST':
        update_form = forms.PostUpdateForm(
            request.POST or None, request.FILES or None)
        if update_form.is_valid():
            post.title = update_form.cleaned_data['title']
            post.content = update_form.cleaned_data['content']
            post.is_published = update_form.cleaned_data['is_published']
            post.image = update_form.cleaned_data['image']
            post.save()

    return render(
        request, 'blog/update_post.html', context={
            'update_form': update_form,
            'post': post
        }
    )


def posts_list(request):
    posts = Post.objects.all()
    return render(
        request, 'blog/posts_list.html', context={
            'posts': posts
        }
    )


def delete_post(request, id):
    delete_form = forms.PostDeleteForm(
        initial={
            'id': id
        }
    )
    if request.method == 'POST':
        delete_form = forms.PostDeleteForm(request.POST or None)
        if delete_form.is_valid():
            Post.objects.get(id=delete_form.cleaned_data['id']).delete()
    return render(
        request, 'blog/delete_post.html', context={
            'delete_form': delete_form
        }
    )


def insert_multipul_posts(request):
    PostFormSet = modelformset_factory(Post, fields='__all__', extra=3)
    insert_multipul_form = PostFormSet(
        request.POST or None, request.FILES or None)
    if insert_multipul_form.is_valid():
        insert_multipul_form.save()
    return render(
        request, 'blog/insert_multipul_posts.html', context={
            'insert_multipul_form': insert_multipul_form
        }
    )
