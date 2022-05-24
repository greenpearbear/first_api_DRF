import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet

from my_project import settings
from .models import Author, Location
from .serializers import LocationSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):
    model = Author

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)

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
class UserDetailView(DetailView):
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
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserPublishedView(ListView):

    model = Author
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):

        super().get(self, request, *args, **kwargs)
        self.object_list = self.object_list.annotate(total_ads=Count('announcement'))

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        users = []

        for user in page_obj:
            users.append({
                'id': user.pk,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'username': user.username,
                'password': user.password,
                'role': user.role,
                'age': user.age,
                'location': list(map(str, user.location.all())),
                'total_ads': user.total_ads
            })

        response = {
            'items': users,
            'total': paginator.count,
            'per_page': paginator.num_pages
        }

        return JsonResponse(response)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
