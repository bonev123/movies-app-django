from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from movieExamDef.accounts.forms import CreateProfileForm, EditProfileForm
from movieExamDef.accounts.models import Profile
from movieExamDef.main.models import Movie, MoviePhoto


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'


class UserRegisterView(CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = list(Movie.objects.filter(user_id=self.object.user_id))

        movie_photos = MoviePhoto.objects \
            .filter(related_movie__in=movies) \
            .distinct()

        total_likes_count = sum(pp.likes for pp in movie_photos)
        total_movie_photos_count = len(movie_photos)

        context.update({
            'total_movie_photos_count': total_movie_photos_count,
            'total_likes_count': total_likes_count,
            'is_owner':  self.request.user.id,
            'movies': movies,
        })
        return context


class ProfileLogoutView(LogoutView):
    template_name = 'accounts/logout_page.html'
    success_url = reverse_lazy('logout user')

class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={
            'pk': self.object.user_id
        })

def error_401(request, exception):
    context = {
        'message': "You are not authorized to show this page. Please create an account or contact the administrator!"
    }
    return render(request, 'main/401_error.html', context=context)
