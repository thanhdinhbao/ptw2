from django.urls import path
from .views import *

urlpatterns = [
    path('import-json/', import_json_from_file, name='import_json'),
    path('add/', add_book, name='add_book'),
    path('', book_list, name='book_list'),
]
