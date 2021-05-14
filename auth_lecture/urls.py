from django.urls import path

from auth_lecture.views import login_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login view'),
    path('logout/', logout_view, name='logout view'),
]
