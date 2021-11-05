from django.shortcuts import render
from .models import Book


# Create your views here.

def listbooks(request):
    book = Book.objects.all()

    context = {
        'books': book,
    }
    return render(request, 'books/list.book.html',context)
