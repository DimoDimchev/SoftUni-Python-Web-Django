from os.path import join

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', include('templates_advanced.urls')),
    path('pets', include('resources.urls')),
    path('auth/', include('auth_lecture.urls')),
    path('cbv/', include('cbv.urls')),
    path('api/books/', include('books_api.urls')),
    path('books/', include('books.urls')),
] + static(settings.MEDIA_URL, document_root=join('media')) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
