from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#IndexPageView with that returns the index.html file

def indexPageView(request) :
    return render(request, 'personpages/index.html')

def aboutPageView(request) :
    return render(request, 'personpages/about.html')

def analysisPageView(request) :
    return render(request, 'personpages/post.html')

def contactPageView(request) :
    return render(request, 'personpages/contact.html')


