from rest_framework import generics

from books_api.models import Book
from books_api.serializers import BookSerializer


class BooksListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BooksDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

