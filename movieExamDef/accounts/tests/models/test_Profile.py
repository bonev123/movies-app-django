from django.core.exceptions import ValidationError
from django.test import TestCase

from movieExamDef.accounts.models import Profile, MoviesUser


class ProfileTests(TestCase):

    TEST_USER_DEFAULT = {
        'username': 'testusertest',
        'password': '649656qweR_lm'
    }

    user = MoviesUser(TEST_USER_DEFAULT)

    user_pk = user.pk
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'username': 'abv',
        'email': 'test@abv.bg',
        'age': 10,
        'picture': 'http://test.picture/url.png',
        'user': user,
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_PROFILE_DATA)
        self.user.save()
        profile.save()
        self.assertIsNotNone(profile.pk)
