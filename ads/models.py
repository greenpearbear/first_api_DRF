from django.db import models


class Categories(models.Model):

    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Location(models.Model):

    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


class Author(models.Model):

    ROLE = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=9, default='member', choices=ROLE)
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Announcement(models.Model):

    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
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




