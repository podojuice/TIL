from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PATCH', 'DELETE'])
def one_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = MovieSerializer(data=request.data, instance=movie)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Movie Edited!'})
        else:
            return R
    else:
        movie.delete()
        return Response({'message': 'Movie Deleted!'})


@api_view(['POST'])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)