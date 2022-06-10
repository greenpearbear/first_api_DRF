import pytest


@pytest.mark.django_db
def test_selection_create(client, user_token, author, announcement):
    response = client.post(
        "/ads/selection/create/",
        {
            "name": "new test selection",
            "owner": author.id,
            "items": [announcement.id]
        },
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Bearer {user_token}")

    assert response.status_code == 201
    assert response.data == {'id': 1, 'name': 'new test selection', 'owner': author.id, 'items': [announcement.id]}