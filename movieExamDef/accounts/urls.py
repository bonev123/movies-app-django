from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from movieExamDef.accounts.views import UserLoginView, UserRegisterView, ProfileDetailsView, \
    ChangeUserPasswordView, ProfileLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
    path('logout/', ProfileLogoutView.as_view(), name='logout user'),

]


