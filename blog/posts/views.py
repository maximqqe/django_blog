from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import Post
from users.models import User


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


class AuthorView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        author = User.objects.get(username=self.kwargs['username'])
        queryset = Post.objects.filter(author=author)
        return queryset


class SearchView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_vector = SearchVector('title', 'content')
        queryset = Post.objects.annotate(search=search_vector).filter(search=query)
        return queryset
