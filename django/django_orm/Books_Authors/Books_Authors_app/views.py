from django.shortcuts import render,redirect,get_object_or_404
from .models import *
def add_book(request):
    context= {
        "all_books": Book.objects.all()
    }
    return render(request, 'add_book.html',context)
def add_this_book(request):
        Book.objects.create(
            title = request.POST['title'],
            desc = request.POST['desc'],
            )
        return redirect('/')
    
def view_books(request, id):
    dict={
        "book_from_data": Book.objects.get(id=int(id)),
        "authores_of_this_book": Book.objects.get(id=int(id)).authors.all(),
        'all_authors' : Author.objects.all(),
        
    }
    return render(request,'view_book.html',dict)
def add_auther_to_this_book(request):
        book_id = int(request.POST['book_id'])
        this_book= Book.objects.get(id=book_id)
        this_book.authors.add(Author.objects.get(id=request.POST["author"]))
        return redirect(f'/view_book/{book_id}')
    
def add_author(request):
    context={
        "all_authors" : Author.objects.all(),
    }
    return render(request,'add_author.html',context)
    
def add_this_author(request):
        Author.objects.create(first_name = request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            notes= request.POST['notes'])
        return redirect('/add_authors')
    

def view_authors(request,id):
    context={
        "author_from_data" : Author.objects.get(id=int(id)),
        "books_for_author" : Author.objects.get(id=int(id)).books.all(),
        "all_books" :Book.objects.all(),
    }
    return render (request,'view_author.html',context)

def add_book_to_this_author(request):
    author_id = int(request.POST['author_id'])
    this_author = Author.objects.get(id=author_id)
    this_book_is=Book.objects.get(id=request.POST['book'])
    this_author.books.add(this_book_is)
    return redirect(f'/view_author/{author_id}')