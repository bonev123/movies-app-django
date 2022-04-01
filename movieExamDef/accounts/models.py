from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.contrib.auth import models as auth_models

from movieExamDef.main.managers import MovieUserManager
from movieExamDef.main.validators import validate_desired_chars


class MoviesUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = MovieUserManager()


class Profile(models.Model):

    CHAR_MIN_LEN = 2
    CHAR_MAX_LEN = 15

    AGE_MIN_VALUE = 0

    first_name = models.CharField(
        max_length=CHAR_MAX_LEN,
    )
    last_name = models.CharField(
        max_length=CHAR_MAX_LEN,
    )
    username = models.CharField(
        max_length=CHAR_MAX_LEN,
        validators=(MinLengthValidator(CHAR_MIN_LEN),
                    validate_desired_chars,
        )
    )
    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )
    picture = models.URLField()

    user = models.OneToOneField(
        MoviesUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

