import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

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
            image=request.FILES["image"],
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
            'image': announcement.image.url,
            'category_id': announcement.category_id

        })


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsGETView(ListView):
    model = Announcement

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        response = []

        self.object_list = self.object_list.order_by('-price')

        for announcement in self.object_list:
            response.append({
                'id': announcement.pk,
                'name': announcement.name,
                'author_id': announcement.author_id,
                'price': announcement.price,
                'description': announcement.description,
                'is_published': announcement.is_published,
                'image': announcement.image.url,
                'category_id': announcement.category_id
            })

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsViewDetail(DetailView):
    model = Announcement

    def get(self, request, *args, **kwargs):
        announcement = self.get_object()

        return JsonResponse({
            'id': announcement.pk,
            'name': announcement.name,
            'author_id': announcement.author_id,
            'price': announcement.price,
            'description': announcement.description,
            'is_published': announcement.is_published,
            'image': announcement.image.url,
            'category_id': announcement.category_id
        })


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsViewUpdate(UpdateView):
    model = Announcement
    fields = ['name', 'price', 'description', 'is_published', 'image', 'author_id', 'category_id']

    def post(self, request, *args, **kwargs):

        super().post(self, request, *args, **kwargs)

        announcement_data = json.loads(request.body)

        self.object.name = announcement_data["name"]
        self.object.price = announcement_data["price"]
        self.object.description = announcement_data["description"]
        self.object.image = request.FILES["image"]
        self.object.category_id = announcement_data["category_id"]

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            'id': self.object.pk,
            'name': self.object.name,
            'author_id': self.object.author_id,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            'image': self.object.image.url,
            'category_id': self.object.category_id
        })


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsViewDelete(DeleteView):
    model = Announcement
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


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


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesGETView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        response = []

        self.object_list = self.object_list.order_by('name')

        for categories in self.object_list:
            response.append({
                'id': categories.pk,
                "name": categories.name,
            })

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesViewDetail(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        categories = self.get_object()

        return JsonResponse({
            'id': categories.pk,
            'name': categories.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesViewUpdate(UpdateView):
    model = Categories
    fields = ['name']

    def post(self, request, *args, **kwargs):

        super().post(self, request, *args, **kwargs)
        categories_data = json.loads(request.body)

        self.object.name = categories_data['name']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            'id': self.object.pk,
            'name': self.object.name

        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesViewDelete(DeleteView):
    model = Categories
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class ImageToAd(UpdateView):
    model = Announcement
    fields = ['name', 'price', 'description', 'is_published', 'image', 'author_id', 'category_id']

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            'id': self.object.pk,
            'name': self.object.name,
            'author_id': self.object.author_id,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            'image': self.object.image.url,
            'category_id': self.object.category_id
        })
