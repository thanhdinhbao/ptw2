# core/urls.py (tạo file nếu chưa có)
from django.urls import path
from .views import (
    ProductList, ProductCreate, ProductDetail,
    ProductUpdate, ProductDelete
)

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:id>/', ProductDetail.as_view(), name='product_detail'),
    path('products/<int:id>/update/', ProductUpdate.as_view(), name='product_update'),
    path('products/<int:id>/delete/', ProductDelete.as_view(), name='product_delete'),
]
