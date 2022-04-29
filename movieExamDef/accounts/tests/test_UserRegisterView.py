from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from movieExamDef.accounts.models import Profile

UserModel = get_user_model()


class UserRegisterViewTest(TestCase):

    VALID_USER_CREDENTIALS = {
        'username': 'testusertest',
        'password': '649656qweR_lm'
    }

    LEGIT_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'abv',
        'email': 'test@abv.bg',
        'age': 10,
        'picture': 'http://test.picture/url.png',
    }

    def __create_user(self, **credentials):
        user = UserModel.objects.create_user(**credentials)
        return user

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.LEGIT_PROFILE_DATA,
            user=user,
        )

        return user, profile

    def __get_response_for_create_profile(self, profile):
        return self.client.get(reverse('dashboard'))

    def __get_response_for_not_create_profile(self):
        return self.client.get(reverse('login user'))

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_user_register__when_input_valid__expect_use_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_create_profile(profile)
        self.assertTemplateUsed('accounts/profile_create.html')

    def test_user_register__when_input_valid__expect_to_create_profile(self):
        _, profile = self.__create_valid_user_and_profile()
        self.assertIsNotNone(profile)
        self.assertEqual(self.LEGIT_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.LEGIT_PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.LEGIT_PROFILE_DATA['username'], profile.username)
        self.assertEqual(self.LEGIT_PROFILE_DATA['email'], profile.email)
        self.assertEqual(self.LEGIT_PROFILE_DATA['age'], profile.age)

    def test_when_opening_not_existing_profile__expect_401(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)
        self.assertTemplateUsed('main/401_error.html')
