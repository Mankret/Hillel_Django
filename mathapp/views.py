import math

from django.shortcuts import render

from mathapp.forms import HypotenuseForm


def triangle(request):

    form = HypotenuseForm(request.GET)
    if form.is_valid():
        f = request.GET.get('f_cath')
        s = request.GET.get('s_cath')
        hyp = math.sqrt(int(f)**2 + int(s)**2)
        return render(request, 'hypotenuse.html', {'hyp': hyp, 'form': form})
    else:
        form = HypotenuseForm()
        return render(request, 'hypotenuse.html', {'form': form})
