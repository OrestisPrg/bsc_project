from django import forms

class Ch1ex1(forms.Form):
    q1 = forms.CharField(label='1: What is the name of the directory you are currently in?', max_length=100)
    q2 = forms.CharField(label='2: How many files/directories are there in the working directory?', max_length=100)
    q3 = forms.CharField(label='3: What is the keyword found in welcome.txt?', max_length=100)
    q4 = forms.CharField(label='4: What is the absolute path of confidential.txt?', max_length=100)
    q5 = forms.ChoiceField(label='5: Which of the following will move welcome.txt in the archive directory?',
      choices=(
      (1, ("mv /archive welcome.txt")),
      (2, ("cd /archive welcome.txt")),
      (3, ("mv welcome.txt /archive")),
      (4, ("cp welcome.txt /archive"))
      ), widget=forms.RadioSelect)
    q6 = forms.CharField(label='6: What command will allow you to edit the file code.c in the archive directory?', max_length=100)
    q7 = forms.ChoiceField(label='7: "cp welcome.txt archive/old_welcome.txt" will create a new copy of welcome.txt in the archive directory',
    choices=(
    (1, ("True")),
    (2, ("False"))
    ))
