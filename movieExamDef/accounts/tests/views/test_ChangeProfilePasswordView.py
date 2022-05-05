from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from movieExamDef.accounts.models import Profile


UserModel = get_user_model()


class ChangeProfilePasswordViewTest(TestCase):

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
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.LEGIT_PROFILE_DATA,
            user=user,
        )
        return user, profile

    def __get_response_for_change_password_profile(self):
        return self.client.get(reverse('change password'))

    def __get_response_password_change_done(self):
        return self.client.get(reverse('password_change_done'))

    def test_user_register__when_input_valid__expect_use_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_change_password_profile()
        self.assertTemplateUsed('accounts/change_password.html')

    def test_change_password__when_password_changed__expect_password_was_changed(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        self.CHANGE_USER_CREDENTIALS = {
            'email': 'test@test.bg',
            'password': '6454Hgggf_',
        }
        response = self.client.post(reverse('change password'), **self.CHANGE_USER_CREDENTIALS )
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('main/dashboard.html')
