from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Max, Min, Sum, Avg
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from docsapp.forms import SendEmailForm
from docsapp.models import Author, Book, Publisher, Store
from docsapp.task import sending_mail


@cache_page(10)
def index(request):
    book_all = Book.objects.count()
    author_all = Author.objects.count()
    publisher_all = Publisher.objects.count()
    store_all = Store.objects.count()

    return render(request, 'docsapp/index.html', context={'book_all': book_all,
                                                          'author_all': author_all,
                                                          'publisher_all': publisher_all,
                                                          'store_all': store_all,
                                                          })


@method_decorator(cache_page(10), "get")
class AuthorView(generic.ListView):
    model = Author
    paginate_by = 200
    template_name = 'docsapp/author.html'

    def get_queryset(self):
        return Author.objects.annotate(Count('book'))


@method_decorator(cache_page(15), "get")
class BookView(generic.ListView):
    model = Book
    paginate_by = 300
    template_name = 'docsapp/book.html'

    def get_queryset(self):
        return Book.objects.annotate(Count('authors'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_aver'] = Book.objects.aggregate(Avg('price'))
        context['book_max'] = Book.objects.aggregate(Max('price'))
        context['book_max_rating'] = Book.objects.aggregate(Max('rating'))
        return context


class PublisherView(generic.ListView):
    model = Publisher
    template_name = 'docsapp/publisher.html'


class StoreView(generic.ListView):
    model = Store
    template_name = 'docsapp/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_price'] = Store.objects.aggregate(min_price=Min('books__price'), max_price=Max('books__price'))
        return context


class AuthorDetailView(generic.DetailView):
    model = Author

    def get_queryset(self):
        return Author.objects.annotate(total_pages=Sum('book__pages'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_count'] = Author.objects.annotate(Count('book'))
        return context


class BookDetailView(generic.DetailView):
    model = Book

    def get_queryset(self):
        return Book.objects.select_related('publisher')


class PublisherDetailView(generic.DetailView):
    model = Publisher

    def get_queryset(self):
        return Publisher.objects.annotate(Count('book'))


class StoreDetailView(generic.DetailView):
    model = Store

    def get_queryset(self):
        return Store.objects.annotate(Count('books'))


def send_email(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['receiving_time']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            more_then_two_days = timezone.now() + timedelta(days=2)
            if time < timezone.now():
                messages.error(request, 'Invalid value! Date cannot be in the past!')
                form = SendEmailForm()
                return render(request, 'send_email.html', {'form': form})
            if time > more_then_two_days:
                messages.error(request, 'Invalid value! Date cannot be more than two days! ')
                form = SendEmailForm()
                return render(request, 'send_email.html', {'form': form})
            sending_mail.apply_async(args=(email, message),
                                     eta=time
                                     )
            return redirect(reverse('docsapp:send_email'))
    else:
        form = SendEmailForm()
    return render(request, 'send_email.html', {'form': form})


class AuthorCreate(LoginRequiredMixin, generic.CreateView):
    model = Author
    fields = ['name', 'age']


class AuthorUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Author
    fields = ['name', 'age']


class AuthorDelete(LoginRequiredMixin, generic.DeleteView):
    model = Author
    success_url = reverse_lazy('docsapp:author')
