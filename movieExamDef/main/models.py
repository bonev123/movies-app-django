from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Movie(models.Model):

    ACTION = 'Action'
    COMEDY = 'Comedy'
    DRAMA = 'Drama'
    FANTASY = 'Fantasy'
    HORROR = "Horror"
    MYSTERY = 'Mystery'
    ROMANCE = 'Romance'
    OTHER = 'Other'
    GENRES = [(x, x) for x in (ACTION, COMEDY, DRAMA, FANTASY, HORROR, MYSTERY, ROMANCE, OTHER)]

    MOVIE_MAX_LEN = 30

    MOVIE_MIN_PRICE = 0.0

    movie_name = models.CharField(
        unique=True,
        max_length=MOVIE_MAX_LEN,
    )
    director = models.CharField(
        max_length=MOVIE_MAX_LEN,
    )

    genre = models.CharField(
        max_length=MOVIE_MAX_LEN,
        choices=GENRES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(verbose_name='Image URL:')

    price = models.FloatField(
        validators=(
            MinValueValidator(MOVIE_MIN_PRICE),
        )
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class MoviePhoto(models.Model):
    photo = models.ImageField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    related_movie = models.ManyToManyField(
        Movie,
    )
    likes = models.IntegerField(
        default=0,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

