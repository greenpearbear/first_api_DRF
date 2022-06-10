import pytest

from tests.factories import AdFactory
from ads.serializers import AnnouncementSerializer


@pytest.mark.django_db
def test_list_view(client):
    vacancies = AdFactory.create_batch(10)

    response = client.get("/ads/ad/")

    assert response.status_code == 200
    assert response.data['results'] == AnnouncementSerializer(vacancies, many=True).data
