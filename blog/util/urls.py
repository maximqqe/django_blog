from django.urls import path

from util.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]