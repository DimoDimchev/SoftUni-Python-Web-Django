from django.urls import path

from cbv.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='cbv index'),
]
