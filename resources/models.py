from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def is_zip_validator(value):
    if not str(value).endswith('.zip'):
        raise ValidationError('Only ZIP files are allowed')


class Pet(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='public/pets')
    # passport = models.FileField(upload_to='private/documents',
    #                             validators=(is_zip_validator,))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
