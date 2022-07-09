from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Books

def index(request):
    books = Books.objects.all()
    return render(request, 'pages/index.html', {'books':books})


def add_book(request):
    title = request.GET.get('title')
    pages = request.GET.get('pages')
    cover = request.FILES.get('cover')
    print(cover)
    author = request.GET.get('author')
    add = Books(title=title, pages=pages, cover=cover, author=author)
    try:
        add.save()
        return HttpResponse('true') 
    except:
        return HttpResponse('false')   


def delete_book(request, id):
    book = get_object_or_404(Books, id=id)
    book.delete()
    return redirect('home')
