from django.contrib.auth import logout, authenticate, login
from django.db import transaction
from django.shortcuts import render, redirect

from auth_lecture.forms import RegisterForm, ProfileForm, LoginForm


@transaction.atomic
def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
            'second_form': ProfileForm(),
        }

        return render(request, 'auth/register.html', context)
    else:
        form = RegisterForm(request.POST)
        second_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and second_form.is_valid():
            user = form.save()
            profile = second_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('pets')

        context = {
            'form': form,
            'second_form': second_form,
        }

        return render(request, 'auth/register.html', context)


def get_redirect_url(params):
    redirect_url = params['return_url']
    if redirect_url == '':
        return 'index'
    return redirect_url


def login_user(request):
    if request.method == 'GET':
        context = {
            'login_form': LoginForm(),
        }

        return render(request, 'auth/login.html', context)
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            return_url = get_redirect_url(request.POST)
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('pets')
            return redirect(return_url)
        else:
            context = {
                'login_form': login_form,
            }
            return render(request, 'auth/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('pets')
