from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('posts.urls', 'posts'), namespace='posts')),
    path('user/', include(('users.urls', 'users'), namespace='user')),
]
