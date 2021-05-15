from django.urls import path

from auth_lecture.views import login_user, logout_user, register_user

urlpatterns = [
    path('login/', login_user, name='login view'),
    path('logout/', logout_user, name='logout view'),
    path('register/', register_user, name='register user'),
]
