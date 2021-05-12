from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='public/pets')
    passport = models.FileField(upload_to='private/documents')

    def __str__(self):
        return self.name
