from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView

from movieExamDef.main.models import Movie
from movieExamDef.rest_api.serializers import MovieListSerializer, MovieFullSerializer


class MovieListAndCreateView(ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
    )

    list_serializer_class = MovieListSerializer
    create_serializer_class = MovieFullSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return self.create_serializer_class
        return self.list_serializer_class
