from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from movieExamDef.accounts.models import Profile
from movieExamDef.main.models import Movie, MoviePhoto

UserModel = get_user_model()


class ProfileDetailsViewTests(TestCase):
    LEGIT_USER_CREDENTIALS = {
        'username': 'testtest',
        'password': '123456asd',
    }

    LEGIT_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'abv',
        'email': 'abv@abv.bg',
        'age': 10,
        'picture': 'http://test.picture/url.png',

    }

    VALID_MOVIE_DATA = {
        'movie_name': 'The movie',
        'director': 'Test',
        'genre': 'action',
        'price': 10,

    }

    VALID_MOVIE_PHOTO_DATA = {
        'photo': 'asd.jpg',

    }

    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.LEGIT_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.LEGIT_PROFILE_DATA,
            user=user,
        )
        return user, profile

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_movie_and_movie_photo_for_user(self, user):
        movie = Movie.objects.create(
            **self.VALID_MOVIE_DATA,
            user=user,
        )
        movie_photo = MoviePhoto.objects.create(
            **self.VALID_MOVIE_PHOTO_DATA,
            user=user,
        )
        movie_photo.related_movie.add(movie)
        movie_photo.save()
        return movie, movie_photo

    def test_show_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_user_is_owner__expect_to_be_true(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.LEGIT_USER_CREDENTIALS)

        response = self.__get_response_for_profile(profile)

        self.assertTrue(response.context['is_owner'])

    def test_when_no_photos__no_photos_count(self):
        user, profile = self.__create_valid_user_and_profile()
        self.__create_movie_and_movie_photo_for_user(user)
        response = self.__get_response_for_profile(profile)

    def test_when_user_has_no_movies__movies_should_be_empty(self):
        _, profile = self.__create_valid_user_and_profile()

        response = self.__get_response_for_profile(profile)
        self.assertListEqual(
            [],
            response.context['movies'],
        )

    def test_when_user_is_not_owner__expect_is_owner_to_be_false(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser',
            'password': '12345qwe',
        }

        self.__create_user(**credentials)

        self.client.login(**credentials)

        response = self.__get_response_for_profile(profile)

        self.assertFalse(response.context['is_owner'])

    def test_when_user_has_movies__expect_to_return_only_user_movie(self):
        user, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser222222',
            'password': '12345qwe',
        }
        user2 = self.__create_user(**credentials)

        movie, _ = self.__create_movie_and_movie_photo_for_user(user)

        self.__create_movie_and_movie_photo_for_user(user2)

        response = self.__get_response_for_profile(profile)

        self.assertListEqual(
            [movie],
            response.context['movies'],
        )


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
