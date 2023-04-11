# In this file we created new view functions that render our HTML templates. 

from django.shortcuts import render
from django.http import HttpResponse
from .models import MissingPerson

# Create your views here.

#IndexPageView with that returns the index.html file

def indexPageView(request) :
    return render(request, 'personpages/index.html')

def aboutPageView(request) :
    return render(request, 'personpages/about.html')

def dataPageView(request) :
    db_persons = MissingPerson.objects.all()
    context = {
        "data" : db_persons
    }
    return render(request, 'personpages/data.html', context)

def displayPageView(request) :
    return render(request, 'personpages/display.html')