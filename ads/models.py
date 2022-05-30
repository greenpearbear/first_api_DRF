from django.db import models

import user.models


class Categories(models.Model):

    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Announcement(models.Model):

    name = models.CharField(max_length=50)
    author = models.ForeignKey(user.models.Author, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)
    is_published = models.CharField(max_length=5)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Selection(models.Model):

    items = models.ManyToManyField(Announcement)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(user.models.Author, on_delete=models.CASCADE)
