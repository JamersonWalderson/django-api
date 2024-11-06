from django.db import models
from uuid import uuid4

# https://docs.djangoproject.com/pt-br/4.0/topics/db/models/
# Create your models here.


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    state = models.CharField(max_length=50)
    pages = models.IntegerField()
    publish_company = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)


class Author(models.Model):
    id_author = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    books = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="authors")