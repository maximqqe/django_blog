from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from posts.form import AddPostForm, CommentForm
from posts.models import Post, PostLike
from users.models import User


class FeedView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            liked_posts = []
            posts = Post.objects.all()
            for post in posts:
                liked = PostLike.objects.filter(user=user, post=post).exists()
                if liked:
                    liked_posts.append(post)
            context['liked_posts'] = liked_posts
        return context


class PostView(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            post = self.object
            liked = PostLike.objects.filter(user=user, post=post).exists()
            context['liked'] = liked
            context['form'] = CommentForm
        return context


class AuthorView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        author = User.objects.get(username=self.kwargs['username'])
        queryset = Post.objects.filter(author=author)
        return queryset


class SearchView(ListView):
    model = Post
    template_name = 'posts/feed.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_vector = SearchVector('title', 'content')
        queryset = Post.objects.annotate(search=search_vector).filter(search=query)
        return queryset


@login_required
def add_post_view(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['author'] = request.user
        form = AddPostForm(data=data)

        if form.is_valid():
            form.save()
            return redirect('posts:feed')
        else:
            print(form.errors)
    form = AddPostForm
    context = {
        'form': form,
    }
    return render(request, 'posts/add_post.html', context=context)


@login_required
def like_post_view(request, post_id):
    post = Post.objects.get(pk=post_id)
    if PostLike.objects.filter(user=request.user, post=post).exists():
        PostLike.objects.filter(user=request.user, post=post).delete()
    else:
        PostLike.objects.create(user=request.user, post=post)

    return redirect(to=request.META['HTTP_REFERER'])


@login_required
def comment_post_view(request, post_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = Post.objects.get(pk=post_id)
        comment.user = request.user
        comment.save()

    return redirect(to='posts:post', pk=post_id)


class LikedPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/liked.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(postlike__user=user)
        return queryset
