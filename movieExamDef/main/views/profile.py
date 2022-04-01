from django.shortcuts import render, redirect

from movieExamDef.accounts.models import Profile
from movieExamDef.main.forms import DeleteProfileForm
from movieExamDef.main.models import Movie


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'main/profile-delete.html', context)


# def show_home(request):
#     profile = get_profile()
#     if not profile:
#         return redirect('create profile')
#     movies = Movie.objects.all()
#
#     context = {
#         'profile': profile,
#         'movies': movies,
#     }
#     return render(request, 'main/home-with-profile.html', context)




# def profile_details(request):
#     profile = get_profile()
#     movies = Movie.objects.all()
#
#     context = {
#         'profile': profile,
#         'movies_count': len(movies),
#     }
#     return render(request, 'main/profile-details.html', context)




# def create_profile(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CreateProfileForm()
#
#     context = {
#         'form': form,
#         'no_profile': True,
#     }
#     return render(request, 'main/home-no-profile.html', context)
