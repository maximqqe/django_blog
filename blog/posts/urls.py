from django.urls import path

from posts.views import FeedView, PostView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
]
