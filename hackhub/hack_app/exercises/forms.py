from django import forms

class Ch1ex1(forms.Form):
  q1 = forms.CharField(label='Which port is responsible for HTTPS?', max_length=100)
  q2 = forms.ChoiceField(label='The directory /.. is the parent directory',
    choices=(
    (1, ("True")),
    (2, ("False"))
    ))
  q3 = forms.ChoiceField(label='What command creates a new file?',
    choices=(
    (1, ("ls")),
    (2, ("cd")),
    (3, ("nano")),
    (4, ("touch"))
    ), widget=forms.RadioSelect)
