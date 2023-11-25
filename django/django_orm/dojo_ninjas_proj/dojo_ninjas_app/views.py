from django.shortcuts import render,redirect
from dojo_ninjas_app.models import *
all_dojos = Dojo.objects.all()

def index(request):
    dojo_dict = {}
    all_dojos = Dojo.objects.all()
    dojo_dict['dojos'] = all_dojos
    return render(request, 'index.html',dojo_dict)

def DojoIn(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
    Dojo.objects.create(name = name, city = city, state=state )
    return redirect('/')

def NinjaIn(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo = request.POST['dojo']
        dojo_object = Dojo.objects.get(id=dojo)
    Ninjas.objects.create(first_name = first_name, last_name = last_name, dojos = dojo_object )
    return redirect('/')
    
