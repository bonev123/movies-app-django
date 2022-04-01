from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from movieExamDef.main.models import MoviePhoto


class MoviePhotoDetailsView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = MoviePhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'movie_photo'

    def get_queryset(self):
        return super() \
            .get_queryset() \
            .prefetch_related('related_movie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context


class CreateMoviePhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = MoviePhoto
    template_name = 'main/photo_create.html'
    fields = ('photo', 'description', 'related_movie')

    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditMoviePhotoView(views.UpdateView):
    model = MoviePhoto
    template_name = 'main/photo_edit.html'
    fields = ('description',)

    def get_success_url(self):
        return reverse_lazy('movie photo details', kwargs={'pk': self.object.id})


