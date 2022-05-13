import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView

from ads.models import Categories, Announcement


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsPOSTView(CreateView):

    model = Announcement
    fields = ['name', 'price', 'description', 'is_published', 'image', 'author_id', 'category_id']

    def post(self, request, *args, **kwargs):

        announcement_data = json.loads(request.body)

        announcement = Announcement.objects.create(
            name=announcement_data["name"],
            price=announcement_data["price"],
            description=announcement_data["description"],
            is_published=announcement_data["is_published"],
            image=announcement_data["image"],
            author_id=announcement_data["author_id"],
            category_id=announcement_data["category_id"]
        )

        return JsonResponse({
            'id': announcement.pk,
            'name': announcement.name,
            'author_id': announcement.author_id,
            'price': announcement.price,
            'description': announcement.description,
            'is_published': announcement.is_published,
            'image': announcement.image,
            'category_id': announcement.category_id

        })


class AnnouncementsGETView(ListView):

    model = Announcement

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        response = []

        for announcement in self.object_list:
            response.append({
                'id': announcement.pk,
                "name": announcement.name,
                'author': announcement.author,
                'price': announcement.price
            })

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesPOSTView(CreateView):

    model = Categories
    fields = ['name']

    def post(self, request, *args, **kwargs):
        categories_data = json.loads(request.body)

        categories = Categories.objects.create(
            name=categories_data['name']
        )

        return JsonResponse({
            'id': categories.pk,
            'name': categories.name
        })


class CategoriesGETView(ListView):

    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        response = []

        for categories in self.object_list:
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
