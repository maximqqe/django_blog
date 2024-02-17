from django.urls import path

from users.views import registration_view, login_view, logout_view, ProfileView

urlpatterns = [
    path('register/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
