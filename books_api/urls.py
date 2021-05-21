from django.urls import path

from books_api.views import BooksAPIView

urlpatterns = [
    path('all/', BooksAPIView.as_view(), name='books list api'),
]
