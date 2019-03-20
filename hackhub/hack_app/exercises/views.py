from django.shortcuts import render
from .forms import Ch1ex1

def ch1ex1(request):
    return render(request, 'exercises/ch1ex1.html')

def ch1qz1(request):
    if request.method == 'POST':
        form = Ch1ex1(request.POST)
    else:
        form = Ch1ex1()
    context = {
        'form': form
    }
    return render(request, 'exercises/ch1ex1_form.html', context)

def ch1ex2(request):
    return render(request, 'exercises/ch1ex2.html')
