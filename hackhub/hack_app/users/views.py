from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can now login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    progress = request.user.progress
    #get a dictionary of progress object's variables and remove unwanted keys
    prog_obj = vars(progress)
    entries = ('_state','id','user_id')
    for key in entries:
        if key in prog_obj:
            del prog_obj[key]
    #calculate the completed percentage from the
    #total number of exercises and the number of completed exercises
    num_ex = len(prog_obj)
    completed = 0
    for x in prog_obj:
        if prog_obj[x] == True:
            completed = completed + 1
    percent = (completed/num_ex)*100
    context = {
        'title': 'My Profile - H|H',
        'u_form': u_form,
        'p_form': p_form,
        'progress': percent,
        'badges': prog_obj
    }
    return render(request, 'users/profile.html', context)
