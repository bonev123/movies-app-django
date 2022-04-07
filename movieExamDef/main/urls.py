from django.urls import path

from movieExamDef.main.views.generic import HomeView, DashboardView
from movieExamDef.main.views.moviePhotos import MoviePhotoDetailsView, CreateMoviePhotoView, EditMoviePhotoView
from movieExamDef.main.views.movies import delete_movie, CreateMovieView, movie_details, edit_movie

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('movie/add/', CreateMovieView.as_view(), name='create movie'),
    path('movie/details/<int:pk>/', movie_details, name='movie details'),
    path('movie/edit/<int:pk>/', edit_movie, name='edit movie'),
    path('movie/delete/<int:pk>/', delete_movie, name='delete movie'),

    path('photo/details/<int:pk>/', MoviePhotoDetailsView.as_view(), name='movie photo details'),
    path('photo/add/', CreateMoviePhotoView.as_view(), name='create movie photo'),
    path('photo/edit/<int:pk>/', EditMoviePhotoView.as_view(), name='edit movie photo'),

]

