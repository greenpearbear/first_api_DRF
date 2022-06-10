from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [

    path('', views.UserListView.as_view(), name='get_list_user'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='get_detail_user'),
    path('create/', views.UserCreateView.as_view(), name='post_user'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete_user'),
    path('Z/', views.UserPublishedView.as_view(), name='get_list_user_published_true'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]


