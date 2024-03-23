from django.contrib import admin

from books.models import Books

# Register your models here.

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_year', 'state', 'pages', 'publish_company', 'create_at')