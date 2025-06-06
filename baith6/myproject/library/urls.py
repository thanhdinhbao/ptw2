# library/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('generate-xml/', generate_xml, name='generate_xml'),
    path('view-xml/', view_xml, name='view_xml'),
    path('recent-books/', recent_books, name='recent_books'),
    path('add-book/', add_book, name='add_book'),
    path('edit-books/', edit_books, name='edit_books'),
]
