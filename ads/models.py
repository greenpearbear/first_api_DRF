from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=25)


class Announcement(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    is_published = models.CharField(max_length=5)

