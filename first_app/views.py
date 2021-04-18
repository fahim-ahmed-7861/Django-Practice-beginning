from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician,Album
from first_app import forms

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

def form(request):
    new_form=forms.user_form()
    diction={'test_form':new_form,'heading_1':"This form is created using django library"}

    if request.method=='POST':
        new_form=forms.user_form(request.POST)

        if new_form.is_valid():
            """
            user_name=new_form.cleaned_data['user_name']
            user_dob=new_form.cleaned_data['user_dob']
            user_email=new_form.cleaned_data['user_email']

            diction.update({'user_name':user_name})
            diction.update({'user_dob':user_dob})
            diction.update({'user_email':user_email})
            """
            diction.update({'field' : new_form.cleaned_data['field']})
            diction.update({'form_submited' : 'Yes'})
    return render(request,'first_app/form.html',context=diction);
