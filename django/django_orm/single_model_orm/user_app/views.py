from django.shortcuts import render,HttpResponse,redirect
from user_app.models import User
from django import forms
def index(request):
    data = User.objects.all()
    print(data)
    print(data[0].first_name)
    dict = {'users' : data}
    return render(request,'index.html',dict)

def form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email= request.POST['email']
        age = request.POST['age']
        User.objects.create(first_name=first_name,last_name=last_name,email_address=email,age=age)
    return redirect('/')

 