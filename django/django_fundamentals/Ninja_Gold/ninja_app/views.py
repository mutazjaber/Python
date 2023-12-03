from django.shortcuts import render,HttpResponse,redirect
from django.urls import path     
import random
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        activity_dict = {}
        request.session['activities'] = activity_dict
    return render(request, 'index.html')

def process(request):
    if request.POST['place'] == "Quest":
        gold = random.randint(-50,50)
        request.session['gold'] += gold
        if gold >0 :    
            request.session['activities'][f"You entered a cave and earned {gold} gold."] = 'green'
        else:request.session['activities'][f"You failed a quest and lost {gold} gold."] = 'red'
        return redirect('/')
    else:
        gold = random.randint(10,20)
        request.session['gold'] += gold
        request.session['activities'][f"You entered a house and earned {gold} gold."] = 'green'
        return redirect('/')
    
def clear_session(request):
    if request.method == 'POST':
        if 'gold' in request.session:
            del request.session['gold']
        if 'activities' in request.session:
            del request.session['activities']
    return redirect('/')
