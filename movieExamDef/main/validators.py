from django.core.exceptions import ValidationError


def validate_desired_chars(value):
    for char in value:
        if not (char.isdigit() or char.isalpha() or char == '_'):
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
