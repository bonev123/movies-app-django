from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from movieExamDef.accounts.models import Profile
from movieExamDef.common.helpers import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.CHAR_MAX_LEN,
    )
    last_name = forms.CharField(
        max_length=Profile.CHAR_MAX_LEN,
    )

    username = forms.CharField(
        max_length=Profile.CHAR_MAX_LEN,
    )

    email = forms.EmailField()
    age = forms.IntegerField()
    picture = forms.URLField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            age=self.cleaned_data['age'],
            picture=self.cleaned_data['picture'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'age')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }
