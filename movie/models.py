from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    image = models.CharField(max_length=600)

    def __str__(self):
        return self.name


class Genre(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class Movies(models.Model):
    movie_name = models.CharField(max_length=250)
    year = models.IntegerField()
    duration = models.CharField(max_length=250)
    ratings = models.IntegerField()
    language = models.CharField(max_length=250)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    poster = models.CharField(max_length=600)

    def __str__(self):
        return self.movie_name


