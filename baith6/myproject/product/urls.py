from django.urls import path
from .views import export_products_to_json, import_products_from_json, product_interface

urlpatterns = [
    path('', product_interface, name='product_interface'),
    path('export/', export_products_to_json, name='export_products'),
    path('import/', import_products_from_json, name='import_products'),
]
