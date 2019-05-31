from django.db import models


class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=10)
    genres = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    poster = models.URLField(default='')
    plot = models.CharField(max_length=500)
    

    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'
class Genre(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    genres = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    poster = models.URLField(default='')

    

    def __str__(self):
        return self.genres + '|' + self.movieid + '|' +self.title

    @staticmethod
    def get_name():
        return 'genre'
class Popularity(models.Model):
    movieid = models.ForeignKey('Movie', default=' ', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    genres = models.IntegerField(default=0)

    def __str__(self):
        return self.movieid.movieid + '|' + str(self.weight) + '|' + str(self.genres)
class GenresPopularity(models.Model):
    #movieid = models.ForeignKey('Movie', default=' ', on_delete=models.CASCADE)
    genres = models.ForeignKey('Genre', default=' ', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    def __str__(self):
        return self.movieid.genres + '|' + str(self.weight)
