# local views
from . import views
# rest framework get token
from rest_framework.authtoken.views import obtain_auth_token
# django urls paths
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(),
         name="search_book"),
    path('<int:pk>', views.BookDelete.as_view(),
         name="delete_book"),
    path('login/', obtain_auth_token, name='auth_login'),
    path('register/', views.SignupViewSet.as_view(), name='auth_register'),
]
