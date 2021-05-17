from django.urls import path

from cbv.views import IndexView, IndexTemplateView, IndexListView

urlpatterns = [
    path('', IndexView.as_view(), name='cbv index'),
    path('2/', IndexTemplateView.as_view(), name='cbv index 2'),
    path('3/', IndexListView.as_view(), name='cbv index 3')
]
