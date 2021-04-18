from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    diction={'text1':'i am a text sent from diction'}
    return render(request,'first_app/index.html',context=diction);

def contact(request):
    return HttpResponse("<h1>contact</h1>")

def about(request):
    return HttpResponse("<h1>About</h1> <a href='/contact/'>Contact</a>  <a href='/'>Home</a>");
