from django.shortcuts import render ,redirect, get_object_or_404
from .models import * 
def index(request):
    context={
        'allshows':Shows.objects.all(),
    }
    print(context)
    return render(request, 'index.html', context)
    
def render_template(request):
    return render(request,'create.html')

def create(request):
    # print("hiiiiiiiiiiiiiiiii")
    # if request.method == "POST":
    title= request.POST['title']
    network=request.POST['network']
    release_date=request.POST['release_date']
    description= request.POST['description']
    newShow=Shows.objects.create(title=title,Network=network,Release_Date=release_date,
                            description=description)
    return redirect(f'/shows/{newShow.id}')


def showTV(request, id ):   
    try:
        show = get_object_or_404(Shows , id=id)
        context ={
            'id':id,
            'title':show.title,
            'network':show.Network,
            'release_date':show.Release_Date,
            'description':show.description,
        }
        return render (request,'show.html',context)
    except :
        return redirect('/')
        


def editShow(request ,id):
    show = get_object_or_404(Shows , id=id)
    context={
            'id':id,
            'title':show.title,
            'network':show.Network,
            'release_date':show.Release_Date,
            'description':show.description,
    }
    return render(request,'edit.html',context)

def update(request):
    id = request.POST['id']
    show = Shows.objects.get(id=request.POST['id'])   
    show.title = request.POST['title']
    show.Network = request.POST['network']
    show.Release_Date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f'/shows/{id}')


def delete(request , id):
    show = Shows.objects.filter(id=id).delete()
    return redirect('/')
    







