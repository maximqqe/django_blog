from django.urls import path

from posts.views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]
