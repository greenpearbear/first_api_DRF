import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Categories, Announcement


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
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

    def get(self, request):

        announcements = Announcement.objects.all()

        response = []

        for announcement in announcements:
            response.append({
                'id': announcement.pk,
                "name": announcement.name,
                'author': announcement.author,
                'price': announcement.price
            })

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def post(self, request):

        categories_data = json.loads(request.body)

        categories = Categories()

        categories.name = categories_data['name']

        categories.save()

        return JsonResponse({
            'id': categories.pk,
            'name': categories.name
        })

    def get(self, request):

        categories = Categories.objects.all()

        response = []

        for categories in categories:
            response.append({
                'id': categories.pk,
                "name": categories.name,
            })

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsViewDetail(DetailView):

    model = Announcement

    def get(self, request, *args, **kwargs):
        announcement = self.get_object()

        return JsonResponse({
                'id': announcement.pk,
                "name": announcement.name,
                'author': announcement.author,
                'price': announcement.price,
                'description': announcement.description,
                'address': announcement.address,
                'is_published': announcement.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesViewDetail(DetailView):

    model = Categories

    def get(self, request, *args, **kwargs):
        categories = self.get_object()

        return JsonResponse({
            'id': categories.pk,
            'name': categories.name
        })
