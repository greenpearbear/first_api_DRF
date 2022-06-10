import pytest


@pytest.mark.django_db
def test_create_ad(client, author, categories, announcement):
    response = client.post("/ads/ad/create/",
                           {
                               "name": "new test ad",
                               "price": 10,
                               "description": "test description",
                               "is_published": "False",
                               "author": announcement.author.pk,
                               "category": announcement.category.pk
                           },
                           content_type="application/json")

    assert response.status_code == 201
    assert response.data == {
        'id': 13,
        'author': announcement.author.pk,
        'category': announcement.category.pk,
        'description': 'test description',
        'image': None,
        'is_published': "False",
        'name': 'new test ad',
        'price': 10,
    }
