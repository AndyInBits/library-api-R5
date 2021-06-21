# locals models
from .models import *
# book models serializers
from .serializers import BookCreateModelSerializer
# celery logger and task
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name='create_book')
def create_book(data):
    """ task for create books async """
    for item in data:
        if 'categories' in item.keys():
            if(len(item['categories']) > 0):
                categories = []
                for cat in item['categories']:
                    obj, created = Category.objects.get_or_create(name=cat)
                    categories.append(obj.pk)
                item['categories'] = categories
        if 'authors' in item.keys():
            if(len(item['authors']) > 0):
                authors = []
                for aut in item['authors']:
                    obj, created = Author.objects.get_or_create(name=aut)
                    authors.append(obj.pk)
                item['authors'] = authors

    serializer_data = BookCreateModelSerializer(data=data, many=True)
    if serializer_data.is_valid():
        serializer_data.save()

    logger.info('Created all books in background !!!')
    return('books created !')
