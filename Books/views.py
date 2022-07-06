from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from .models import Books

def index(request):
    books = Books.objects.all()
    return render(request, 'pages/index.html', {'books':books})


def add_book(request):
    title = request.POST.get('title')
    pages = request.POST.get('pages')
    cover = request.FILES.get('cover')
    author = request.POST.get('author')
    add = Books(title=title, pages=pages, cover=cover, author=author)
    add.save()    
    return redirect('home')


def delete_book(request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return redirect('home')
