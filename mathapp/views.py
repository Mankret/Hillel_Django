import math

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from mathapp.forms import HypotenuseForm, PersonCreateForm
from mathapp.models import Person


class IndexView(generic.ListView):
    model = Person
    template_name = 'mathapp/index.html'

    def get_queryset(self):
        return Person.objects.all()


class DetailView(generic.DetailView):
    model = Person
    template_name = 'mathapp/detail.html'
    context_object_name = 'person'


def triangle(request):

    form = HypotenuseForm(request.GET)
    if form.is_valid():
        f = request.GET.get('f_cath')
        s = request.GET.get('s_cath')
        hyp = math.sqrt(int(f) ** 2 + int(s) ** 2)
        return render(request, 'hypotenuse.html', {'hyp': hyp, 'form': form})
    else:
        form = HypotenuseForm()
        return render(request, 'hypotenuse.html', {'form': form})


def person_create(request):
    if request.method == "POST":
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(reverse('mathapp:detail', args=(obj.id,)))
    else:
        form = PersonCreateForm()
    return render(request, "mathapp/person_create.html", {"form": form})


def person_update(request, pk):
    obj = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('mathapp:index'))
    else:
        form = PersonCreateForm(instance=obj)
    return render(request, 'mathapp/person_update.html', {'form': form, 'obj': obj})
