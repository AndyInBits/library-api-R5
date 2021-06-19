# Django
from django.db import models

# Utilities
from utils.models import CommonModel


class Category(CommonModel):
    """category model.

    Model to store the data of the categories of the books.
    """
    name = models.TextField(
        'category name',
        max_length=255,
        blank=False,
        null=False,
        help_text="category name"
    )

    def __str__(self):
        """Return name category."""
        return self.name
