from django.contrib.auth import get_user_model
from django.db import models
from users.models import User


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.SET(get_sentinel_user))

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.title} | {self.created_at}'
