
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'utils.pagination.CustomPagination',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
