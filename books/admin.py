from django.contrib import admin

from books.models import Author, Books

# Register your models here.

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'state', 'pages', 'publish_company', 'create_at')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'books')