from django.shortcuts import render
from rest_framework import views as rest_views
from rest_framework.response import Response

from books_api.models import Book
from books_api.serializers import BookSerializer


class BooksAPIView(rest_views.APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
