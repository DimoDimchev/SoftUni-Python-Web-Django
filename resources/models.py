from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='pets')
    passport = models.FileField(upload_to='documents')

    def __str__(self):
        return self.name
