# Django
from django.db import models

# Utilities
from utils.models import CommonModel


class Author(CommonModel):
    """Author model.

    Model to store the data of the authors of the books.
    """
    name = models.CharField(
        'name',
        max_length=150,
        blank=False,
        null=False,
        help_text="Name author"
    )

    def __str__(self):
        """Return name author."""
        return self.name
