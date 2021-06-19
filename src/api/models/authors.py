# Django
from django.db import models

# Utilities
from utils.models import CommonModel


class Author(CommonModel):
    """Author model.

    Model to store the data of the authors of the books.
    """
    first_name = models.CharField(
        'first name',
        max_length=150,
        blank=False,
        null=False,
        help_text="Name author"
    )
    last_name = models.CharField(
        'last name',
        max_length=150,
        blank=False,
        null=False,
        help_text="Name author"
    )

    def __str__(self):
        """Return name author."""
        return self.first_name

    def get_full_name(self):
        """Return full name author."""
        return '{} {}'.format(self.first_name, self.last_name)
