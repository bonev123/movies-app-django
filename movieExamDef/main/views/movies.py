from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from movieExamDef.main.forms import CreateMovieForm, EditMovieForm, DeleteMovieForm
from movieExamDef.main.models import Movie


class CreateMovieView(CreateView):
    template_name = 'main/add-movie.html'
    form_class = CreateMovieForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


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
