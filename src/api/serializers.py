# django rest framework serializers
from rest_framework import serializers

# local models
from .models import *


class CategoryModelSerializer(serializers.ModelSerializer):
    """Category model serializer."""

    class Meta:
        """Meta class."""
        model = Category
        fields = ('name',)


class AuthorModelSerializer(serializers.ModelSerializer):
    """Author model serializer."""
    class Meta:
        """Meta class."""
        model = Author
        fields = ('get_full_name',)


class BookModelSerializer(serializers.ModelSerializer):
    """Book model serializer."""
    authors = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)

    class Meta:
        """Meta class."""
        model = Book
        fields = (
            'title',
            'sub_title',
            'publish_date',
            'editor',
            'description',
            'image',
            'source_book',
            'authors',
            'categories',
            'created',
            'modified'
        )
