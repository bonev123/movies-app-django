from django.shortcuts import redirect, render

from movieExamDef.main.forms import CreateMovieForm, EditMovieForm, DeleteMovieForm
from movieExamDef.main.models import Movie


def create_movie(request):
    if request.method == 'POST':
        form = CreateMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateMovieForm()

    context = {
        'form': form,

    }
    return render(request, 'main/add-movie.html', context)


def edit_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditMovieForm(instance=movie)

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'main/edit-movie.html', context)


def delete_movie(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteMovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteMovieForm(instance=movie)

    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'main/delete-movie.html', context)


def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'main/movie-details.html', context)
