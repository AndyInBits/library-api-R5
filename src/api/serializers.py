# django rest framework serializers
from rest_framework import serializers

# local models
from .models import *


class BookModelSerializer(serializers.ModelSerializer):
    """Book model serializer."""
    authors = serializers.StringRelatedField(many=True, read_only=False)
    categories = serializers.StringRelatedField(many=True, read_only=False)

    class Meta:
        """Meta class."""
        model = Book
        fields = fields = '__all__'


class BookCreateModelSerializer(serializers.ModelSerializer):
    """Book create model serializer."""

    class Meta:
        """Meta class."""
        model = Book
        fields = fields = '__all__'

    def create(self, validated_data):
        """ overwrite method create of serializer """

        authors = validated_data.pop('authors')
        categories = validated_data.pop('categories')
        books = Book.objects.create(**validated_data)
        for auth in authors:
            books.authors.add(auth)
        for cat in categories:
            books.categories.add(cat)
        return books
