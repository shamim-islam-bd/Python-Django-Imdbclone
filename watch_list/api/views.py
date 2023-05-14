from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from watch_list.api.serializers import Movie

# Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }

#     return JsonResponse(data)


@api_view()
def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }

    return JsonResponse(data)


@api_view()
def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    data = {
        'movie': {
            'name': movie.name,
            'description': movie.description,
            'active': movie.active
        }
    }

    return JsonResponse(data)
    
   