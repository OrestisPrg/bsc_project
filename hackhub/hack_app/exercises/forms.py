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

class Ch1ex2(forms.Form):
    q1 = forms.CharField(label='1: What is the permissions string for passwords.txt?', max_length=100)
    q2 = forms.CharField(label='2: What is the last password in passwords.txt?', max_length=100)
    q3 = forms.CharField(label='3: What is the new permission string for passwords.txt?', max_length=100)
    q4 = forms.ChoiceField(label='4: Which of the following commands will grant you permission to modify passwords.txt?',
      choices=(
      (1, ("sudo chmod +w passwords.txt")),
      (2, ("sudo chmod o+w passwords.txt")),
      (3, ("sudo chmod u+w passwords.txt")),
      (4, ("sudo chmod g+w passwords.txt"))
      ), widget=forms.RadioSelect)
    q5 = forms.ChoiceField(label='5: "sudo chown root new.txt" will make root the owner of new.txt',
    choices=(
    (1, ("True")),
    (2, ("False"))
    ))

class Ch1ex3(forms.Form):
    q1 = forms.ChoiceField(label='1: A hacker with no permission to penetrate a system is considered ethical, if their intentions are good.',
    choices=(
    (1, ("True")),
    (2, ("False"))
    ))
    q2 = forms.ChoiceField(label='2: Both ethical and malicious hackers follow a generally similar approach when it comes to compromising a system.',
    choices=(
    (1, ("True")),
    (2, ("False"))
    ))
    q3 = forms.ChoiceField(label='3: During footprinting, hackers need to acquire the system\'s owner\'s credentials in order to be able to gain access to the target system.',
    choices=(
    (1, ("True")),
    (2, ("False"))
    ))
    q4 = forms.ChoiceField(label='4: During which stage the hacker will ideally be able to use the system\'s root user account first?',
      choices=(
      (1, ("Clearing Tracks")),
      (2, ("Gaining Access")),
      (3, ("Maintaining Access")),
      (4, ("Footprinting"))
      ), widget=forms.RadioSelect)

class Ch2ex1(forms.Form):
    q1 = forms.CharField(label='1: Perform a scan on a UDP ports. Which port is open? Please provide its number.', max_length=100)
