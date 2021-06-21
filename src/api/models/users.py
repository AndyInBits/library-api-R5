"""User model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from utils.models import CommonModel


class User(CommonModel, AbstractUser):
    """User model.

    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    def __str__(self):
        """Return email."""
        return self.email
