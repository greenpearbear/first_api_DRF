from django.http import JsonResponse
from django.views import View


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


