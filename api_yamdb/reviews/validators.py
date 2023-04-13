import datetime

from django.core.exceptions import ValidationError


def year_validator(value):
    year = datetime.date.today().year
    if year < value:
        raise ValidationError('Год не может быть меньше текущего')
    return value
