from django.forms import ModelForm
from .models import Ticket
from django import forms



class Createticket(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'steps_reproduce', 'num_of_ppl_affected', 'url', 'assignee']


class Edit(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'steps_reproduce', 'status', 'num_of_ppl_affected', 'url', 'assignee']

class Datepicker(forms.Form):
    from_date = forms.DateField()
    to_date = forms.DateField()