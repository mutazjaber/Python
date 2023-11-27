from django.shortcuts import render

def add_book(request):
    return render(request, 'add_book.html')