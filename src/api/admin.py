"""User models admin."""

# Django
from django.contrib import admin

# Models
from .models import *


class BookAdmin(admin.ModelAdmin):
    """Book model admin."""
    list_display = ('pk', 'title', 'sub_title', 'publish_date',
                    'editor', 'description', 'image')
    list_filter = ('title', 'authors', 'categories')


class AuthorAdmin(admin.ModelAdmin):
    """Author model admin."""
    list_display = ('pk', 'first_name', 'last_name',)
    list_filter = ('first_name', 'last_name', )


class CategoryAdmin(admin.ModelAdmin):
    """Category model admin."""
    list_display = ('pk', 'name',)
    list_filter = ('name', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
