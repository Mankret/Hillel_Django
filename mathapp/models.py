from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=120, unique=True)

    def __str__(self):
        return f'{self.first_name}'


class LogModel(models.Model):
    path = models.CharField(max_length=200, null=True)
    method = models.CharField(max_length=120, null=True)
    create = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=120, null=True)
    title = models.CharField(max_length=60, default='Log')
    query = models.TextField(null=True)
    body = models.TextField(null=True)

    def __str__(self):
        return self.title
