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
        'title': 'Homepage'
    }
    return render(request,'hackme/home.html',context)

@login_required
def about(request):
    context = {
        'title': 'About'
    }
    return render(request,'hackme/about.html', context)

@login_required
def chapters(request):
    context = {
        'title': 'Chapters'
    }
    return render(request,'hackme/chapters.html', context)
