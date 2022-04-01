from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from movieExamDef.accounts.forms import CreateProfileForm
from movieExamDef.accounts.models import Profile
from movieExamDef.main.models import Movie


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
    template_name = 'main/../../templates/accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        movies = list(Movie.objects.filter(user_id=self.object.user_id))

        context.update({
            'is_owner':  self.request.user.id,
            'movies': movies,
        })
        return context
