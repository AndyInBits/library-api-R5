# local views
from . import views

# django urls paths
from django.urls import path

urlpatterns = [
    path('search', views.BookList.as_view(),
         name="search_book"),
]
