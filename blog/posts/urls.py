from django.urls import path

from posts.views import FeedView, PostView, AuthorView, SearchView, add_post_view, like_post_view, comment_post_view

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('author/<slug:username>/', AuthorView.as_view(), name='author'),
    path('search/', SearchView.as_view(), name='search'),
    path('add/', add_post_view, name='add_post'),
    path('like/<int:post_id>', like_post_view, name='like'),
    path('comment/<int:post_id>', comment_post_view, name='comment')
]
