from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)

    # author = models.ForeignKey(to=User)

    class Meta:
        db_table = 'post'
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.title} | {self.created_at}'
