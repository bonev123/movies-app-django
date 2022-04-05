import unittest
from django.core.exceptions import ValidationError

from movieExamDef.common.validators import validate_file_max_size_in_mb


class FakeFile:
    size = 5


class FakeImage:
    file = FakeFile()


class ValidateFileMaxSizeInMbTests(unittest.TestCase):
    def test_when_file_is_bigger__expect_to_raise(self):
        validator = validate_file_max_size_in_mb(0.000001)

        file = FakeImage()

        with self.assertRaises(ValidationError) as context:
            validator(file)

        self.assertIsNotNone(context.exception)

    def test_when_file_size_is_valid__expect_to_do_nothing(self):
        validator = validate_file_max_size_in_mb(1)

        file = FakeImage()

        validator(file)
