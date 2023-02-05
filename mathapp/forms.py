from django import forms

from mathapp.models import Person


class HypotenuseForm(forms.Form):
    f_cath = forms.IntegerField(label='First Catheus', min_value=1)
    s_cath = forms.IntegerField(label='Second Catheus', min_value=1)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]
