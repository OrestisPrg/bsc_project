from django.shortcuts import render

def ch1ex1(request):
    return render(request, 'exercises/ch1ex1.html')

def ch1ex2(request):
    return render(request, 'exercises/ch1ex2.html')
