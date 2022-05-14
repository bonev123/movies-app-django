from django.contrib import admin
from movieExamDef.accounts.models import Profile, MoviesUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(MoviesUser)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_superuser')
