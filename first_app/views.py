from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album

# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name');

    diction={'text1':'i am a text sent from diction',
    'musician' : musician_list}
    return render(request,'first_app/index.html',context=diction);

def contact(request):
    return HttpResponse("<h1>contact</h1>")

def about(request):
    return HttpResponse("<h1>About</h1> <a href='/contact/'>Contact</a>  <a href='/'>Home</a>");
