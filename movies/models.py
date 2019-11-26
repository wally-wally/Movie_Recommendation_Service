from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    poster_url = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField()
    audience_rating = models.CharField(max_length=100)
    audience = models.IntegerField()
    genre_id = models.ManyToManyField(Genre, related_name='genre_movies', blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    release_date = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-pk',)


class Comment(models.Model):
    content = models.CharField(max_length=150)
    score = models.IntegerField(
        validators = [MinValueValidator(0), MaxValueValidator(10)]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-pk',)


class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=50)    
    profile_photo = models.TextField()
    def __str__(self):
        return self.name