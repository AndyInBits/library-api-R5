# local models
from .models import *

# local Book model serializers
from .serializers import BookModelSerializer

# django rest framework generics views
from rest_framework.generics import ListAPIView, DestroyAPIView

# django rest framework filter
from rest_framework import filters

# external services consult book
from .services import get_books_external_api

# cache libs
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# local task create books
from .tasks import create_book


class BookList(ListAPIView):
    """ Book list api view """
    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        return super(BookList, self).dispatch(*args, **kwargs)

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
        'authors__name',
        'categories__name'
    ]
    ordering_fields = ['title', ]

    def filter_queryset(self, queryset):
        """ overwrite method filter_queryset to add functionality y validation of response """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        if len(queryset) <= 0:
            queryset = get_books_external_api(
                self.request.query_params['search'])
            create_book.delay(queryset)
        return queryset


class BookDelete(DestroyAPIView):
    queryset = Book.objects.all()
