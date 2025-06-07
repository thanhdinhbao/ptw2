from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator
from django.db.models import Q

from django.http import HttpResponse
from django.conf import settings
import os, json
from .serializers import BookSerializer

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'T2022601124/add_book.html', {'form': form})

def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all()
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    
    paginator = Paginator(books, 3)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    return render(request, 'T2022601124/book_list.html', {'books': books})

def import_json_from_file(request):
    file_path = os.path.join(settings.BASE_DIR, 'books.json')
    
    if not os.path.exists(file_path):
        return HttpResponse("❌ File books.json không tồn tại.", status=404)

    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            return HttpResponse(f"❌ JSON không hợp lệ: {e}", status=400)
    
    count = 0
    for item in data:
        serializer = BookSerializer(data=item)
        if serializer.is_valid():
            serializer.save()
            count += 1
        else:
            return HttpResponse(f"❌ Lỗi ở bản ghi: {serializer.errors}", status=400)

    return HttpResponse(f"✅ Đã thêm {count} bản ghi từ books.json")

