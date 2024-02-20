from django import forms

from posts.models import Post, PostComment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['text', ]
