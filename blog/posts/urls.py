from django.urls import path

from posts.views import FeedView, PostView, AuthorView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('author/<slug:username>/', AuthorView.as_view(), name='author'),
]
