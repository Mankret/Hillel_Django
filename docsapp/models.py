from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('docsapp:author_detail', args=[str(self.pk)])

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('docsapp:publisher_detail', args=[str(self.pk)])

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField(auto_now=True, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('docsapp:book_detail', args=[str(self.pk)])

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def get_absolute_url(self):
        return reverse('docsapp:store_detail', args=[str(self.pk)])

    def __str__(self):
        return self.name
