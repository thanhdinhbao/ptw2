from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator
from django.db.models import Q

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
