from django.urls import path

from resources.views import resources

urlpatterns = [
    path('', resources, name='pets')
]
