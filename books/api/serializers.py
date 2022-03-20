# https://labcodes.com.br/blog/pt-br/development/como-usar-serializers-de-django-rest-framework/

import rest_framework import serializers
from Books import models

class BooksSerializer(serializers.ModelSeriealizer):
  class Meta:
    model = models.Books
    fields = '__ALL__'
