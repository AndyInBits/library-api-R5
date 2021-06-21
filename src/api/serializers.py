# local models
from .models import *

# model user default django
from django.contrib.auth.models import User

# Django REST Framework
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers


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


class SignupSerializer(serializers.ModelSerializer):
    """ register serializer """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(
                                         queryset=User.objects.all())]
                                     )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password', 'email',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
