from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
