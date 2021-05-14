from django.contrib.auth import logout
from django.shortcuts import render, redirect


def login_view(request):
    pass


def logout_view(request):
    logout(request)
    return redirect('pets')
