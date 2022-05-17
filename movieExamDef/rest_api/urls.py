from django.urls import path

from movieExamDef.rest_api.views import MovieListAndCreateView

urlpatterns = [
    path('movies/', MovieListAndCreateView.as_view(), name='api list or create movie'),
]
