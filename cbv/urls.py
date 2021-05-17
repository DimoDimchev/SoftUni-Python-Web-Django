from django.urls import path

from cbv.views import IndexView, IndexTemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='cbv index'),
    path('2/', IndexTemplateView.as_view(), name='cbv index 2'),
]
