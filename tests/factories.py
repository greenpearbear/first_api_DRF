import factory

from ads.models import Announcement, Categories
from user.models import Author


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categories

    slug = factory.Faker("color")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    username = factory.Faker('name')
    age = 10


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Announcement

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 10
