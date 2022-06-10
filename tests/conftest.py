from pytest_factoryboy import register
from factories import UserFactory, AdFactory, CategoryFactory

pytest_plugins = "tests.fixtures"

register(UserFactory)
register(AdFactory)
register(CategoryFactory)
