from django.core.exceptions import ValidationError
from django.test import TestCase

from movieExamDef.accounts.models import Profile, MoviesUser


class ProfileTests(TestCase):
    def setUp(self) -> None:
        self.TEST_USER_DEFAULT = {
            'username': 'testusertest',
            'password': '649656qweR_lm_'
        }
        self.user = MoviesUser(**self.TEST_USER_DEFAULT)

        self.user_pk = self.user.pk
        self.VALID_PROFILE_DATA = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'abv',
            'email': 'test@abv.bg',
            'age': 10,
            'picture': 'http://test.picture/url.png',
            'user': self.user,
        }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        self.user.save()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Alex2'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            username=self.VALID_PROFILE_DATA['username'],
            email=self.VALID_PROFILE_DATA['email'],
            age=self.VALID_PROFILE_DATA['age'],
            picture=self.VALID_PROFILE_DATA['picture'],
            user=self.user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            self.user.save()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_under_line__expect_to_fail(self):
        first_name = 'Alex_'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            username=self.VALID_PROFILE_DATA['username'],
            email=self.VALID_PROFILE_DATA['email'],
            age=self.VALID_PROFILE_DATA['age'],
            picture=self.VALID_PROFILE_DATA['picture'],
            user=self.user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            self.user.save()
            profile.save()

        self.assertIsNotNone(context.exception)
