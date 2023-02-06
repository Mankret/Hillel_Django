from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=120, unique=True)

    def __str__(self):
        return f'{self.first_name}'
