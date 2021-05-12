from django.urls import path

from resources.views import resources, serve_private_files

urlpatterns = [
    path('', resources, name='pets'),
    path('resources/', serve_private_files, name='private files')
]
