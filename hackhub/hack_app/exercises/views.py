from django.shortcuts import render
from .forms import Ch1ex1, Ch1ex2, Ch1ex3, Ch2ex1
from .models import Answers
from users.models import Progress
#from django.core.exceptions import ValidationError

def ex_completed(request):
    return render(request, 'exercises/ex_completed.html')

def ch1ex1(request):
    context = {
        'title': 'Section 1.1 - H|H'
    }
    return render(request, 'exercises/ch1ex1.html', context)

def ch1qz1(request):
    quiz = '1.1'
    failed = False
    if request.method == 'POST':
        form = Ch1ex1(request.POST)
        if form.is_valid():
            #q1 = form.cleaned_data['q1']
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    print(q)
                    failed = True
                    # show which is wrong
            if failed:
                return render(request, 'exercises/ch1ex1_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch1ex1 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch1ex1()
    context = {
        'title': 'Quiz 1.1 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch1ex1_form.html', context)

def ch1ex2(request):
    context = {
        'title': 'Section 1.2 - H|H'
    }
    return render(request, 'exercises/ch1ex2.html', context)

def ch1qz2(request):
    quiz = '1.2'
    failed = False
    if request.method == 'POST':
        form = Ch1ex2(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch1ex2_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch1ex2 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch1ex2()
    context = {
        'title': 'Quiz 1.2 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch1ex2_form.html', context)

def ch1ex3(request):
    context = {
        'title': 'Section 1.3 - H|H'
    }
    return render(request, 'exercises/ch1ex3.html', context)

def ch1qz3(request):
    quiz = '1.3'
    failed = False
    if request.method == 'POST':
        form = Ch1ex3(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch1ex3_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch1ex3 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch1ex3()
    context = {
        'title': 'Quiz 1.3 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch1ex3_form.html', context)

def ch2ex1(request):
    context = {
        'title': 'Section 2.1 - H|H'
    }
    return render(request, 'exercises/ch2ex1.html', context)

def ch2qz1(request):
    quiz = '2.1'
    failed = False
    if request.method == 'POST':
        form = Ch2ex1(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch2ex1_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch2ex1 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch2ex1()
    context = {
        'title': 'Quiz 2.1 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch2ex1_form.html', context)
