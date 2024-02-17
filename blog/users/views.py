import os

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from blog.settings import BASE_DIR
from users.forms import RegistrationForm, LoginForm, ProfileChangeForm
from users.models import User


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)

        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return redirect(to='posts:feed')
    else:
        form = RegistrationForm

    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                if request.POST.get('next', None):
                    return redirect(to=request.POST.get('next'))

                return redirect(to='posts:feed')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'users/login.html', context=context)


@login_required
def logout_view(request):
    auth.logout(request)
    return redirect(to='posts:feed')


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'


@login_required
def profile_change_view(request):
    if request.method == "POST":
        form = ProfileChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            if 'image' in request.FILES:
                file_path = BASE_DIR / request.user.image.url
                if os.path.exists(file_path):
                    os.remove(file_path)

                request.user.image = request.FILES['image']
            request.user.save()

            return redirect(to='user:profile', pk=request.user.pk)

    else:
        form = ProfileChangeForm()

    context = {
        'form': form,
    }

    return render(request, template_name='users/change.html', context=context)

