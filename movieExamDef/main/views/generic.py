from django.views.generic import TemplateView, ListView

from movieExamDef.common.view_mixins import RedirectToDashboard
from movieExamDef.main.models import MoviePhoto


class HomeView(RedirectToDashboard, TemplateView):
    template_name = 'main/home-no-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(ListView):
    model = MoviePhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'movie_photos'
