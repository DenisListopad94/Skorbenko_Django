from django.core.exceptions import ValidationError


def age_validator(age):
    if age < 18 or age > 90:
        raise ValidationError(
            f" Age {age} should be between 18 & 90"
        )
