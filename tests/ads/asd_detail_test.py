import pytest


@pytest.mark.django_db
def test_ad_detail(client, announcement, author, user_token):

    expected_response = {
        "id": announcement.pk,
        "name": '',
        'author': author.pk,
        'price': 10,
        'description': None,
        'is_published': '',
        'image': None,
        'category': 11
    }

    response = client.get(f"/ads/ad/{announcement.pk}/",
                          content_type="application/json",
                          HTTP_AUTHORIZATION=f"Bearer {user_token}")

    assert response.status_code == 200
    assert response.data == expected_response
