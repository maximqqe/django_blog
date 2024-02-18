from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('posts.urls', 'posts'), namespace='posts')),
    path('user/', include(('users.urls', 'users'), namespace='user')),
    path('', include(('util.urls', 'util'), namespace='util'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
