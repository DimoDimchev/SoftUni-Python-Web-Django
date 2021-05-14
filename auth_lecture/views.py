from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    username = 'test_user'
    password = 'testpwd123'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('pets')

    return redirect('pets')


def logout_view(request):
    logout(request)
    return redirect('pets')
