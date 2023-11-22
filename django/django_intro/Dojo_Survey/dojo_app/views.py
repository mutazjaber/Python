from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')


def result(request):
    if request.method == 'POST':
        name=request.POST["username"]
        location=request.POST["location"]
        language=request.POST["language"]
        text=request.POST["Comment"]
    dict={
        'name': name,
        'location':location,
        'language': language,
        'text':text,
    }
    return render(request,'result.html',dict)
    
    
    
