from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms

# Create your views here.

def index(request):
    musician_list=Musician.objects.order_by('first_name');

    diction={'text1':'i am a text sent from diction',
    'musician' : musician_list,'sample_date' : Album.objects.get(pk=1)}
    return render(request,'first_app/index.html',context=diction);

def contact(request):
    return HttpResponse("<h1>contact</h1>")

def about(request):
    return HttpResponse("<h1>About</h1> <a href='/contact/'>Contact</a>  <a href='/'>Home</a>");

def form(request):
    new_form=forms.MusicianForm()



    if request.method=='POST':
        new_form = forms.MusicianForm(request.POST)


        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction={'test_form' : new_form,'heading_1': 'Add New Musician'}

    return render(request,'first_app/form.html',context=diction);
