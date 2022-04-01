from django import forms
from django.shortcuts import render

from movieExamDef.accounts.models import Profile
from movieExamDef.main.models import Movie


# class CreateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('username', 'email', 'age', 'picture')

class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        #image_path = self.instance.image.path
        self.instance.delete()
        Movie.objects.all().delete()
        #os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()

class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name', 'director', 'genre', 'description', 'image_url', 'price')


class EditMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name', 'director', 'genre', 'description', 'image_url', 'price')


class DeleteMovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Movie
        fields = ('movie_name', 'director', 'genre', 'description', 'image_url', 'price')

class MovieDetails(forms.ModelForm):
    def get_movie(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        return render(request, "main/movie-details.html", {"movie": movie})
