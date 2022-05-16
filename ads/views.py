import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from ads.models import Categories, Announcement, Author
from my_project import settings


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsCreateView(CreateView):
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
class AnnouncementsListView(ListView):
    model = Announcement

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object_list = None

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        self.object_list = self.object_list.order_by('-price')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        announcements = []
        for announcement in page_obj:
            announcements.append({
                'id': announcement.pk,
                'name': announcement.name,
                'author_id': announcement.author_id,
                'price': announcement.price,
                'description': announcement.description,
                'is_published': announcement.is_published,
                'image': announcement.image.url,
                'category_id': announcement.category_id
            })

        response = {
            'items': announcements,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AnnouncementsDetailView(DetailView):
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
class AnnouncementsUpdateView(UpdateView):
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
class AnnouncementsDeleteView(DeleteView):
    model = Announcement
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesCreateView(CreateView):
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
class CategoriesListView(ListView):
    model = Categories

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object_list = None

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
class CategoriesDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        categories = self.get_object()

        return JsonResponse({
            'id': categories.pk,
            'name': categories.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesUpdateView(UpdateView):
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
class CategoriesDeleteView(DeleteView):
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


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):

    model = Author

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.object_list = None

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

        self.object_list = self.object_list.order_by('username')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        authors = []

        for author in page_obj:
            authors.append({
                'id': author.pk,
                'first_name': author.first_name,
                'last_name': author.last_name,
                'username': author.username,
                'password': author.password,
                'role': author.role,
                'age': author.age,
                'location': list(self.object.location.all().values_list('name', flat=True))
            })

        response = {
            'items': authors,
            'total': paginator.count,
            'num_pages': paginator.num_pages
        }

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserViewDetail(DetailView):

    model = Author

    def get(self, request, *args, **kwargs):

        author = self.get_object()

        return JsonResponse({
            'id': author.pk,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'username': author.username,
            'password': author.password,
            'role': author.role,
            'age': author.age,
            'location': list(self.object.location.all().values_list('name', flat=True))
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):

    model = Author
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']

    def post(self, request, *args, **kwargs):

        user_data = json.loads(request.body)

        author = Author.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            username=user_data['username'],
            password=user_data['password'],
            role=user_data['role'],
            age=user_data['age'],
            location=user_data['location']
        )

        return JsonResponse({
            'id': author.pk,
            'first_name': author.first_name,
            'last_name': author.last_name,
            'username': author.username,
            'password': author.password,
            'role': author.role,
            'age': author.age,
            'location': list(self.object.location.all().values_list('name', flat=True))
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):

    model = Author
    fields = ['first_name', 'last_name', 'username', 'password', 'role', 'age', 'location']

    def post(self, request, *args, **kwargs):

        super().post(self, request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.first_name = user_data['first_name']
        self.object.last_name = user_data['last_name']
        self.object.username = user_data['username']
        self.object.password = user_data['password']
        self.object.role = user_data['role']
        self.object.age = user_data['age']
        self.object.location = user_data['location']

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            'id': self.object.pk,
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'username': self.object.username,
            'password': self.object.password,
            'role': self.object.role,
            'age': self.object.age,
            'location': list(self.object.location.all().values_list('name', flat=True))
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):

    model = Author

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
