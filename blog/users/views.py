from django.contrib import auth
from django.shortcuts import render, redirect

from users.forms import RegistrationForm, LoginForm


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


def logout_view(request):
    auth.logout(request)
    return redirect(to='posts:feed')
