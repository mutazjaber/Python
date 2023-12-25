from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/')
    fName = request.POST['first_name']
    lName = request.POST['last_name']
    email =  request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    conPassword = request.POST['confrim_password']
    new_user = User.objects.create(firstName = fName, lastName = lName, email = email, password = pw_hash)
    request.session['id']  = new_user.id
    return redirect('/dashboard')

def success(request):
    if "id" in request.session:
        user = User.objects.get(id = request.session['id'])
        context = {
            "user" : user
        }
        return render(request, "welcome.html", context)
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value) 
        return redirect('/')
    email = request.POST["email"]
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/dashboard')
    else:
        messages.error(request,"User is not Exist")
    return redirect('/')

def logout(request):
    del request.session['id']
    return redirect("/")

def add_pie(request):
    errors = Pie.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')
    else:
        name = request.POST['name']
        filling = request.POST['filling']
        crust = request.POST['crust']
        my_user = User.objects.get(id = request.session['id'])
        new_pie = Pie.objects.create(name = name,  filling = filling ,crust=crust , my_user = my_user)
        content = {
            'pies' :Pie.objects.all(),
            'current_user' : my_user
        }
        return redirect('/dashboard')

def user_dashboard(request):
    my_user = User.objects.get(id=request.session['id'])
    context = {
        'current_user': my_user,
        'pies': Pie.objects.all(), 
        'pie_user':Pie.objects.last()
    }
    return render(request, "welcome.html", context)
def  delete(request,id):
    pie = Pie.objects.get(id=id)
    pie.delete()
    return redirect('/dashboard')



def show_pies(request):
    my_user = User.objects.get(id = request.session['id'])
    pies = Pie.objects.all()
    content = {
        'pies' : pies,
        'current_user' : my_user
    }
    return render(request,'view.html',content)

def edit_form(request, id):
    pies = Pie.objects.get(id=id)
    my_user = User.objects.get(id = request.session['id'])
    content = {
        'pies' : pies,
        'current_user' : my_user
    }
    return render(request, 'edit.html',content)

def edit_process(request, id):
    name = Pie.objects.get(id = id).name
    errors = Pie.objects.basic_validator(request.POST)
    if len(errors) > 0 :
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit_pie/{id}')
    else:
        pie = Pie.objects.get(id = id)
        pie.name = request.POST['name']
        pie.filling = request.POST['filling']
        pie.crust = request.POST['crust']
        pie.save()

        return redirect('/dashboard')
    


def view_pie(request,id):
    my_user = User.objects.get(id = request.session['id'])
    pie = Pie.objects.get(id = id)
    content = {
        'pie' : pie,
        'current_user' : my_user
    }
    return render(request, 'view_pie.html', content)

def add_vote(request,id):
    user = User.objects.get(id = request.session['id'])
    pie = Pie.objects.get(id = id)
    if request.POST['which_form'] == 'add':
        pie.vote.add(user)

    elif request.POST['which_form'] == 'remove':
        pie.vote.remove(user)
    return render(request, 'view.html')


