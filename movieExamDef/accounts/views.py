from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from movieExamDef.accounts.forms import CreateProfileForm
from movieExamDef.accounts.models import Profile
from movieExamDef.main.models import Movie, MoviePhoto


class UserLoginView(LoginView):
    template_name = 'accounts/login_page-test.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'


class UserRegisterView(CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create-test.html'
    success_url = reverse_lazy('dashboard')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details-test.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = list(Movie.objects.filter(user_id=self.object.user_id))

        movie_photos = MoviePhoto.objects \
            .filter(related_movie__in=movies) \
            .distinct()

        total_movie_photos_count = len(movie_photos)


        context.update({
            'movie_photos_count': total_movie_photos_count,
            'is_owner':  self.request.user.id,
            'movies': movies,
        })
        return context


# def delete_profile(request):
#     return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')
