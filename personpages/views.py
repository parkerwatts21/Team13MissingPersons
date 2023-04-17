# In this file we created new view functions that render our HTML templates and imported render and model. 

from django.shortcuts import render
from django.http import HttpResponse
from .models import MissingPerson

# Create your views here.

#IndexPageView with that returns the index.html file

def indexPageView(request) :
    return render(request, 'personpages/index.html')

def aboutPageView(request) :
    return render(request, 'personpages/about.html')

# This returns the missing persons data from the database to be displayed on the data page

def dataPageView(request) :
    db_persons = MissingPerson.objects.all()
    context = {
        "data" : db_persons
    }
    return render(request, 'personpages/data.html', context)

# This returns a missing persons specific data with their given id

def detailPageView(request, id) :
    person = MissingPerson.objects.get(id=id)
    context = {
        "data" : person
    }
    return render(request,'personpages/detailPage.html', context)