import factory

from ads.models import Announcement, Categories
from user.models import Author


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categories

    slug = factory.Faker("name")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    username = factory.Faker('name')
    age = 10


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Announcement

    category = factory.SubFactory(CategoriesFactory)
    author = factory.SubFactory(UserFactory)
    price = 10
