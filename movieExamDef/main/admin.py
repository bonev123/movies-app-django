from django.contrib import admin

from movieExamDef.main.models import Movie, MoviePhoto


class MovieInlineAdmin(admin.StackedInline):
    model = Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'genre')


@admin.register(MoviePhoto)
class MoviePhotoAdmin(admin.ModelAdmin):
    pass

