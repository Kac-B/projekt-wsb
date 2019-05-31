from django.contrib import admin
from movie.models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'movieid','genres','length', 'rate', 'year')
admin.site.register(Movie, MovieAdmin)

