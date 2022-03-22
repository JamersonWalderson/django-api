from rest_framework.response import Response
from rest_framework import viewsets
from books.api import serializers
from books import models

class BooksViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.BooksSerializer
  queryset = models.Books.objects.all()


  def create(self, request):
    return Response( {'message': 'Livro cadastrado com sucesso.'})