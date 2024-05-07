import datetime
from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    all_books = Book.objects.all()
    context = {'books': all_books}
    for book in all_books:
        book.pub_date = str(book.pub_date)
        print(f'{book.name=} - {book.pub_date=}')
    return render(request, template, context)

def pagi_books_view(request, dt):
    template = 'books/books_p_list.html'
    print(f'{dt=}')
    
    books_ = Book.objects.filter(pub_date=dt)
    print(f'{books_=}')
    
    next_book = Book.objects.filter(pub_date__gt=dt).order_by('pub_date').first()
    prev_book = Book.objects.filter(pub_date__lt=dt).order_by('-pub_date').first()
    
    if next_book:
        print(f'{next_book=}, {next_book.pub_date=}')
        next_book = str(next_book.pub_date)
    if prev_book:
        print(f'{prev_book=}, {prev_book.pub_date=}')
        prev_book = str(prev_book.pub_date)
    
    context = {
        'books': books_,
        'next_book': next_book,
        'prev_book': prev_book,
    }
    return render(request, template, context)
    
