# local models
from .models import *

# local Book model serializers
from .serializers import BookModelSerializer

# django rest framework generics views
from rest_framework.generics import ListAPIView

# django rest framework filter
from rest_framework import filters

# external services consult book
from .services import get_books_external_api

# asynnc io
import asyncio

loop = asyncio.get_event_loop()


class BookList(ListAPIView):
    """ Book list api view """

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'id',
        'title',
        'sub_title',
        'publish_date',
        'editor',
        'description',
        'image',
        'source_book',
        'authors__first_name',
        'authors__last_name',
        'categories__name'
    ]
    ordering_fields = ['title', ]

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with whichever filter backend is in use.

        You are unlikely to want to override this method, although you may need
        to call it either from a list view, or from a custom `get_object`
        method if you want to apply the configured filtering backend to the
        default queryset.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        if len(queryset) <= 0:
            print("voy a consultar a los apis")
            argument = self.request.query_params['search']
            queryset = get_books_external_api(argument)

        return queryset
