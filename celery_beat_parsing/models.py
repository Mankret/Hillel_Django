from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=120)
    born = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Quotes(models.Model):
    quote = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.quote}'
