from django.shortcuts import render
# from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def welcome(request):
    context = {
        'title': 'Welcome to HackHub'
    }
    return render(request, 'hackme/welcome.html', context)

@login_required
def home(request):
    context = {
        'title': 'Homepage - H|H'
    }
    return render(request,'hackme/home.html',context)

@login_required
def about(request):
    context = {
        'title': 'Get Started - H|H'
    }
    return render(request,'hackme/about.html', context)

@login_required
def chapters(request):
    context = {
        'title': 'Chapters - H|H'
    }
    return render(request,'hackme/chapters.html', context)

@login_required
def references(request):
    context = {
        'title': 'References - H|H'
    }
    return render(request,'hackme/references.html', context)
