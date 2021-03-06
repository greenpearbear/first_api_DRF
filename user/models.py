from django.contrib.auth.models import AbstractUser
from django.db import models


class Location(models.Model):

    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class Author(AbstractUser):

    ROLE = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=500)
    role = models.CharField(max_length=9, default='member', choices=ROLE)
    age = models.IntegerField()
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
