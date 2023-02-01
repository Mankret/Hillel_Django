from django.db import models


class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text


class Country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Developer(models.Model):
    title = models.CharField(max_length=120)
    industry = models.CharField(max_length=120)
    country = models.OneToOneField("Country", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.title},{self.industry}'


class Game(models.Model):
    title = models.CharField(max_length=120)
    developer = models.ForeignKey("Developer", on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
