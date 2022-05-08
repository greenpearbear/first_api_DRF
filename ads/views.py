import json

from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from ads.models import Categories, Announcement


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class CategoriesViewList(ListView):

    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []

        for categories in self.object_list:
            response.append({
                'id': categories.pk,
                "name": categories.name,
            })

        return JsonResponse(response, safe=False)


class AnnouncementViewList(ListView):

    model = Announcement

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []

        for announcement in self.object_list:
            response.append({
                'id': announcement.pk,
                "name": announcement.name,
                'author': announcement.author,
                'price': announcement.price
            })

        return JsonResponse(response, safe=False)


class AnnouncementsView(View):
    def post(self, request):

        announcement_data = json.loads(request.body)

        announcement = Announcement()
        announcement.name = announcement_data["name"]
        announcement.author = announcement_data["author"]
        announcement.price = announcement_data["price"]
        announcement.description = announcement_data["description"]
        announcement.address = announcement_data["address"]
        announcement.is_published = announcement_data["is_published"]

        announcement.save()

        return JsonResponse({
            'id': announcement.pk,
            'name': announcement.name,
            'author': announcement.author,
            'price': announcement.price,
            'description': announcement.description,
            'address': announcement.address,
            'is_published': announcement.is_published

        })


class CategoriesView(View):
    def post(self, request):

        categories_data = json.loads(request.body)

        categories = Categories()

        categories.name = categories_data['name']

        return JsonResponse({
            'id': categories.pk,
            'name': categories.name
        })
