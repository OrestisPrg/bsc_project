from django.shortcuts import render
from .forms import Ch1ex1
from .models import Answers
from users.models import Progress
#from django.core.exceptions import ValidationError

def ex_completed(request):
    return render(request, 'exercises/ex_completed.html')

def ch1ex1(request):
    return render(request, 'exercises/ch1ex1.html')

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
        'form': form
    }
    return render(request, 'exercises/ch1ex1_form.html', context)

def ch1ex2(request):
    return render(request, 'exercises/ch1ex2.html')
