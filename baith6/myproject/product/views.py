# products/views.py
import os, json
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .serializers import ProductSerializer

JSON_PATH = os.path.join(settings.MEDIA_ROOT, 'json', 'products.json')

def export_products_to_json(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(serializer.data, f, ensure_ascii=False, indent=4)
    return redirect('product_interface')

def import_products_from_json(request):
    if not os.path.exists(JSON_PATH):
        return HttpResponse("Chưa có file products.json")

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    added = 0
    for item in data:
        if not Product.objects.filter(id=item['id']).exists():
            serializer = ProductSerializer(data=item)
            if serializer.is_valid():
                serializer.save()
                added += 1
    return redirect('product_interface')

def product_interface(request):
    products = Product.objects.all()
    return render(request, 'product/interface.html', {'products': products})