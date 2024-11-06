# https://labcodes.com.br/blog/pt-br/development/como-usar-serializers-de-django-rest-framework/
# https://youtu.be/wtl8ZyCbTbg?t=787

from email.policy import default
from platform import release
from typing_extensions import Required
from rest_framework import serializers
from books import models
import random


def random_page():
    return str(random.randrange(0, 999))


def random_release_year():
    return str(random.randrange(1900, 2022))


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class BooksSerializer(serializers.ModelSerializer):
    title = serializers.CharField(default="lorem ipsum")
    author = serializers.CharField(default="lorem ipsum")
    state = serializers.CharField(default="lorem ipsum")
    publish_company = serializers.CharField(default="lorem ipsum")
    pages = serializers.IntegerField(default=random_page)
    release_year = serializers.IntegerField(default=random_release_year)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = models.Books
        fields = [
            "id_book",
            "title",
            "author",
            "release_year",
            "state",
            "pages",
            "publish_company",
            "create_at",
            "authors",
        ]