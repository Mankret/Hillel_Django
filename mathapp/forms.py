from django import forms


class HypotenuseForm(forms.Form):
    f_cath = forms.IntegerField(label='First Catheus', min_value=1)
    s_cath = forms.IntegerField(label='Second Catheus', min_value=1)

