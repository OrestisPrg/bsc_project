from django.shortcuts import render
from .forms import *
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


def ch2ex2(request):
    context = {
        'title': 'Section 2.2 - H|H'
    }
    return render(request, 'exercises/ch2ex2.html', context)


def ch2qz2(request):
    quiz = '2.2'
    failed = False
    if request.method == 'POST':
        form = Ch2ex2(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch2ex2_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch2ex2 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch2ex2()
    context = {
        'title': 'Quiz 2.2 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch2ex2_form.html', context)

def ch2ex3(request):
    context = {
        'title': 'Section 2.3 - H|H'
    }
    return render(request, 'exercises/ch2ex3.html', context)

def ch2qz3(request):
    quiz = '2.3'
    failed = False
    if request.method == 'POST':
        form = Ch2ex3(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch2ex3_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch2ex3 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch2ex3()
    context = {
        'title': 'Quiz 2.3 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch2ex3_form.html', context)

def ch2ex4(request):
    context = {
        'title': 'Section 2.4 - H|H'
    }
    return render(request, 'exercises/ch2ex4.html', context)

def ch2qz4(request):
    quiz = '2.4'
    failed = False
    if request.method == 'POST':
        form = Ch2ex4(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch2ex4_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch2ex4 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch2ex4()
    context = {
        'title': 'Quiz 2.4 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch2ex4_form.html', context)


def ch3ex1(request):
    context = {
        'title': 'Section 3.1 - H|H'
    }
    return render(request, 'exercises/ch3ex1.html', context)


def ch3qz1(request):
    quiz = '3.1'
    failed = False
    if request.method == 'POST':
        form = Ch3ex1(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch3ex1_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch3ex1 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch3ex1()
    context = {
        'title': 'Quiz 3.1 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch3ex1_form.html', context)

def ch3ex2(request):
    context = {
        'title': 'Section 3.2 - H|H'
    }
    return render(request, 'exercises/ch3ex2.html', context)


def ch3qz2(request):
    quiz = '3.2'
    failed = False
    if request.method == 'POST':
        form = Ch3ex2(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch3ex2_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch3ex2 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})

    else:
        form = Ch3ex2()
    context = {
        'title': 'Quiz 3.2 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch3ex2_form.html', context)

def ch3ex3(request):
    context = {
        'title': 'Section 3.3 - H|H'
    }
    return render(request, 'exercises/ch3ex3.html', context)

def ch3qz3(request):
    quiz = '3.3'
    failed = False
    if request.method == 'POST':
        form = Ch3ex3(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch3ex3_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch3ex3 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})
    else:
        form = Ch3ex3()
    context = {
        'title': 'Quiz 3.3 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch3ex3_form.html', context)

def ch3ex4(request):
    context = {
        'title': 'Section 3.4 - H|H'
    }
    return render(request, 'exercises/ch3ex4.html', context)

def ch3qz4(request):
    quiz = '3.4'
    failed = False
    if request.method == 'POST':
        form = Ch3ex4(request.POST)
        if form.is_valid():
            answers = Answers.objects.get(quiz=quiz)

            for q in form.cleaned_data:
                if form.cleaned_data[q] != getattr(answers,q):
                    failed = True
            if failed:
                return render(request, 'exercises/ch3ex4_form.html', {'form': form})
            else:
                progress = request.user.progress
                progress.ch3ex4 = True
                progress.save()
                return render(request, 'exercises/ex_completed.html', {'exercise': quiz})
    else:
        form = Ch3ex4()
    context = {
        'title': 'Quiz 3.4 - H|H',
        'form': form
    }
    return render(request, 'exercises/ch3ex4_form.html', context)
