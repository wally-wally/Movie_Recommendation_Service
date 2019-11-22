from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=150)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    overview = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='genre_movies', blank=True)