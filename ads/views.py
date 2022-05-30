import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ads.models import Categories, Announcement, Selection
from .serializers import AnnouncementSerializer, SelectionSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import SelectionPermissions, AdminOrModeratorPermissions

def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AnnouncementListView(ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def get(self, request, *args, **kwargs):

        category = request.GET.get('cat', None)
        text = request.GET.get('text', None)
        location = request.GET.get('location', None)
        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)

        if category:
            self.queryset = self.queryset.filter(category_id=category)

        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        if price_to and price_from:
            self.queryset = self.queryset.filter(price__lte=price_to).filter(price__gte=price_from)

        return super().get(self, request, *args, **kwargs)


class AnnouncementRetrieveView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]


class AnnouncementCreateView(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class AnnouncementUpdateView(UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, AdminOrModeratorPermissions]


class AnnouncementDestroyView(DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated, AdminOrModeratorPermissions]


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


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionPermissions]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionPermissions]


class SelectionDestroyView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionPermissions]

