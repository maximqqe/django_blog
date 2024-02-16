from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import Post


class FeedView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by("-id")


class PostView(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'
