from django.urls import path

from movieExamDef.main.views.generic import HomeView, DashboardView
from movieExamDef.main.views.moviePhotos import MoviePhotoDetailsView, CreateMoviePhotoView, EditMoviePhotoView
from movieExamDef.main.views.movies import create_movie, movie_details, edit_movie, delete_movie
from movieExamDef.main.views.profile import delete_profile

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('movie/add/', create_movie, name='create movie'),
    path('movie/details/<int:pk>/', movie_details, name='movie details'),
    path('movie/edit/<int:pk>/', edit_movie, name='edit movie'),
    path('movie/delete/<int:pk>/', delete_movie, name='delete movie'),

    path('photo/details/<int:pk>/', MoviePhotoDetailsView.as_view(), name='movie photo details'),
    path('photo/add/', CreateMoviePhotoView.as_view(), name='create movie photo'),
    path('photo/edit/<int:pk>/', EditMoviePhotoView.as_view(), name='edit movie photo'),

    #path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),

]

