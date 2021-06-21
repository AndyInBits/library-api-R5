# Django
from django.db import models

# Utilities
from utils.models import CommonModel

# local models
from .authors import Author
from .categories import Category


class Book(CommonModel):
    """Book model.
    Model to store the data of books.
    """
    title = models.CharField(
        'book title',
        max_length=255,
        blank=True,
        null=True,
        help_text="Book title"
    )
    sub_title = models.CharField(
        'book sub title',
        max_length=255,
        blank=True,
        null=True,
        help_text="Book sub title"
    )

    publish_date = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )
    editor = models.CharField(
        'book editor',
        max_length=150,
        blank=True,
        null=True,
        help_text="Book editor"
    )

    description = models.TextField(
        'book description',
        blank=True,
        null=True,
        help_text="Book description"
    )

    image = models.TextField(
        'book image',
        blank=True,
        null=True,
        help_text="Book image"
    )

    source_book = models.CharField(
        'book source',
        max_length=30,
        blank=True,
        null=True,
        help_text="Book source"
    )

    authors = models.ManyToManyField(Author, blank=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        """Return title book."""
        return self.title
