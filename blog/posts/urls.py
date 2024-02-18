from django.urls import path

from posts.views import FeedView, PostView, AuthorView, SearchView, add_post_view

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('author/<slug:username>/', AuthorView.as_view(), name='author'),
    path('search/', SearchView.as_view(), name='search'),
    path('add/', add_post_view, name='add_post')
]
