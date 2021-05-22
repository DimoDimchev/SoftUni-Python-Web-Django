from django.urls import path

from books_api.views import BooksListAPIView, BooksDetailsAPIView

urlpatterns = [
    path('', BooksListAPIView.as_view(), name='books list api'),
    path('<int:pk>/', BooksDetailsAPIView.as_view(), name='books details api')
]
