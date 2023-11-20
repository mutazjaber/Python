from django.shortcuts import render,redirect,HttpResponse

def index(request):
   return redirect ('/blogs')

def root(request):
    return HttpResponse(
        "placeholder to later display a list of all blogs" 
    )

def new(request):
    return HttpResponse(
        "placeholder to display a new form to create a new blog"
    )