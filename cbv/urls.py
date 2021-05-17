from django.urls import path

from cbv.views import IndexView, IndexTemplateView, IndexListView, IndexDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='cbv index'),
    path('2/', IndexTemplateView.as_view(), name='cbv index 2'),
    path('list/', IndexListView.as_view(), name='cbv index 3'),
    path('details/<int:pk>', IndexDetailView.as_view(), name='cbv index 4')
]
