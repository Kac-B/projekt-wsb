from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from movie.models import *
import operator
import random
from movie.initializer import search_index


@csrf_protect
def index(request):
    data = {}
    movie_dict = search_index.data_in_memory['movie_dict']
    popular_movies = Popularity.objects.all().order_by('-weight')# wg popularności (ilości z bazy danych)
    popular = []
    for movie in popular_movies[:5]:
        try:
            popular.append({'movieid': movie.movieid_id, 'poster': movie_dict[movie.movieid_id].poster}) #poster
        except:
            continue
    data['popular'] = popular
    popular_movie_list = [movie_dict[movie.movieid_id] for movie in popular_movies[:5]]
    data['recommendation'] = get_recommendation(request, popular_movie_list)
    return render(request, 'base.html', data)


def get_recommendation(request, popular_movie_list):
    result = []
    movie_dict = search_index.data_in_memory['movie_dict']
    added_movie_list = []
    if request.user.is_authenticated:

        genre_stats = {}
        movie_score = {}
        for item in sorted_list:
            movie = movie_dict[item[0]]
            result.append({'movieid': movie.movieid, 'poster': movie.poster})
            added_movie_list.append(movie)
            if len(result) == 8:
                break
    sorted_list = sorted(search_index.data_in_memory['movie_rating'].items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_list:
        movie = movie_dict[item[0]]
        if movie not in popular_movie_list and movie not in added_movie_list:
            result.append({'movieid': movie.movieid, 'poster': movie.poster})
        if len(result) == 10:
            break
    return [result[i] for i in random.sample(range(len(result)), 5)]
