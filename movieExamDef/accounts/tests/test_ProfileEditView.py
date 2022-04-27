from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from movieExamDef.accounts.models import Profile


UserModel = get_user_model()


class ProfileEditViewTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuserbg',
        'password': '63576Hgdh_kd',
    }

    LEGIT_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'abv',
        'email': 'abv@abv.bg',
        'age': 10,
        'picture': 'http://test.picture/url.png',
    }

    def __create_user(self, **credentials):
        user = UserModel.objects.create_user(**credentials)
        return user

    def __create_valid_user_and_profile_edit_view(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.LEGIT_PROFILE_DATA,
            user=user,
        )

        return user, profile

    def __get_response_for_edit_profile(self, profile):
        return self.client.post(reverse('profile details',  kwargs={'pk': profile.pk}))

    def test_profile_edit__when_input_valid__expect_use_correct_template(self):
        _, profile = self.__create_valid_user_and_profile_edit_view()
        self.__get_response_for_edit_profile(profile)
        self.assertTemplateUsed('accounts/profile_details.html')
