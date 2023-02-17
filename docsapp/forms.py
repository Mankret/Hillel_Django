from django import forms
from django.utils import timezone


class SendEmailForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Text reminder', required=True)
    receiving_time = forms.DateTimeField(label='When should be sent', help_text='write date and time')
