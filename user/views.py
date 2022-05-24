from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from my_project import settings
from .models import Author, Location
from .serializers import LocationSerializer, AuthorSerializer


class UserListView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserDetailView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserCreateView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserUpdateView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserDeleteView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


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


class UserPublishedViewAPI(ListAPIView):
    queryset = Author.objects.filter()
    serializer_class = AuthorSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
