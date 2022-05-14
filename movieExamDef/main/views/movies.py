from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from movieExamDef.common.view_mixins import RedirectPermissionRequiredMixin
from movieExamDef.main.forms import CreateMovieForm, EditMovieForm, DeleteMovieForm, DetailsMovieForm
from movieExamDef.main.models import Movie


class CreateMovieView( CreateView):
    #permission_required = ('main.add_movie',)
    template_name = 'main/add-movie.html'
    form_class = CreateMovieForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditMovieView(UpdateView):
    template_name = 'main/edit-movie.html'
    form_class = EditMovieForm

# def edit_movie(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = EditMovieForm(request.POST, instance=movie)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = EditMovieForm(instance=movie)
#
#     context = {
#         'form': form,
#         'movie': movie,
#     }
#     return render(request, 'main/edit-movie.html', context)


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


class DetailsMovieView(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = 'main/movie-details.html'
    form_class = DetailsMovieForm
    context_object_name = 'movie'
    permission_required = ('main.movie-details',)

