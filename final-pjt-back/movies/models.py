from django.db import models
from django.conf import settings
# Create your models here.


class Boxoffice(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    audiAcc = models.IntegerField()
    overview = models.TextField(null=True)
    vote_average = models.FloatField(null=True)
    independent = models.BooleanField()
    poster_path = models.TextField()
    release_date = models.TextField(null=True)



class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    profile = models.TextField(null=True)


class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    profile = models.TextField(null=True)


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    adult = models.BooleanField(default=False, null=True)
    independent = models.BooleanField(null=True)
    release_date = models.TextField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.TextField(null=True)
    original_language = models.CharField(max_length=10, null=True)
    genres = models.CharField(max_length=30, null=True)
    vote_average = models.FloatField(null=True)
    runtime = models.IntegerField(null=True)
    ott_service = models.CharField(max_length=100, null=True)
    backdrops = models.TextField(null=True)
    playlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='playlist_movie')
    watch = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watch_movie')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie')
    actors = models.ManyToManyField(Actor, related_name='act_movie')
    directors = models.ManyToManyField(Director,related_name='direct_movie')

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hashtag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='hashtag')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='hashtag')
    tag = models.CharField(max_length=100)
