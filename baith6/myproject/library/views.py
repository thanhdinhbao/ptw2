# library/views.py
from django.http import HttpResponse
from xml.etree.ElementTree import Element, SubElement, ElementTree
import os
from django.conf import settings
import xml.etree.ElementTree as ElementTree
from django.shortcuts import render, redirect

XML_PATH = os.path.join(settings.MEDIA_ROOT, 'xml', 'books.xml')

def generate_xml(request):
    library = Element('library')

    books = [
        {"title": "Django for Beginners", "author": "William S. Vincent", "year": "2022"},
        {"title": "Two Scoops of Django", "author": "Daniel Roy Greenfeld", "year": "2021"},
        {"title": "Python Crash Course", "author": "Eric Matthes", "year": "2020"},
        {"title": "Fluent Python", "author": "Luciano Ramalho", "year": "2019"},
        {"title": "Effective Python", "author": "Brett Slatkin", "year": "2015"},
        {"title": "Clean Code", "author": "Robert C. Martin", "year": "2008"},
        {"title": "Think Python", "author": "Allen B. Downey", "year": "2023"},
        {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "year": "2020"},
    ]

    for book in books:
        book_elem = SubElement(library, 'book')
        SubElement(book_elem, 'title').text = book["title"]
        SubElement(book_elem, 'author').text = book["author"]
        SubElement(book_elem, 'year').text = book["year"]

    xml_path = os.path.join(settings.MEDIA_ROOT, 'xml', 'books.xml')
    tree = ElementTree.ElementTree(library)
    os.makedirs(os.path.dirname(xml_path), exist_ok=True)
    tree.write(xml_path, encoding='utf-8', xml_declaration=True)

    return HttpResponse("Đã tạo file books.xml thành công!")

def view_xml(request):
    xml_path = os.path.join(settings.MEDIA_ROOT, 'xml', 'books.xml')

    try:
        tree = ElementTree.parse(xml_path)
        root = tree.getroot()
    except Exception as e:
        return HttpResponse(f"Lỗi đọc file XML: {e}")

    books = []
    for book in root.findall('book'):
        books.append({
            'title': book.find('title').text,
            'author': book.find('author').text,
            'year': book.find('year').text,
        })

    return render(request, 'library/view_xml.html', {'books': books})

def recent_books(request):
    xml_path = os.path.join(settings.MEDIA_ROOT, 'xml', 'books.xml')

    try:
        tree = ElementTree.parse(xml_path)
        root = tree.getroot()
    except Exception as e:
        return HttpResponse(f"Lỗi đọc file XML: {e}")

    books = []
    for book in root.findall('book'):
        try:
            year = int(book.find('year').text)
            if year >= 2020:
                books.append({
                    'title': book.find('title').text,
                    'author': book.find('author').text,
                    'year': year
                })
        except:
            continue  # bỏ qua nếu dữ liệu sai

    return render(request, 'library/recent_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')

        try:
            tree = ElementTree.parse(XML_PATH)
            root = tree.getroot()
        except:
            root = ElementTree.Element('library')
            tree = ElementTree.ElementTree(root)

        # Thêm sách mới
        book_elem = ElementTree.SubElement(root, 'book')
        ElementTree.SubElement(book_elem, 'title').text = title
        ElementTree.SubElement(book_elem, 'author').text = author
        ElementTree.SubElement(book_elem, 'year').text = year

        # Ghi lại file
        os.makedirs(os.path.dirname(XML_PATH), exist_ok=True)
        tree.write(XML_PATH, encoding='utf-8', xml_declaration=True)

        return redirect('edit_books')

    return render(request, 'library/add_book.html')

def edit_books(request):
    try:
        tree = ElementTree.parse(XML_PATH)
        root = tree.getroot()
    except:
        return HttpResponse("Chưa có file books.xml hoặc lỗi định dạng.")

    # Xử lý xóa sách
    if request.method == 'POST':
        delete_title = request.POST.get('delete_title')
        for book in root.findall('book'):
            if book.find('title').text == delete_title:
                root.remove(book)
                break
        tree.write(XML_PATH, encoding='utf-8', xml_declaration=True)
        return redirect('edit_books')

    # Lấy danh sách sách
    books = []
    for book in root.findall('book'):
        books.append({
            'title': book.find('title').text,
            'author': book.find('author').text,
            'year': book.find('year').text,
        })

    return render(request, 'library/edit_books.html', {'books': books})