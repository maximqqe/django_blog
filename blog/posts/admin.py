from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_fields = ('title', 'created_at')
    list_search = ('title', 'description')
