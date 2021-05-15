from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

from auth_lecture.forms import RegisterForm


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
        }

        return render(request, 'auth/register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pets')

        context = {
            'form': form,
        }

        return render(request, 'auth/register.html', context)


def login_user(request):
    username = 'test_user'
    password = 'testpwd123'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('pets')

    return redirect('pets')


def logout_user(request):
    logout(request)
    return redirect('pets')
