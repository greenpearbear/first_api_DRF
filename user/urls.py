from django.urls import path
from . import views

urlpatterns = [

    path('', views.UserListView.as_view(), name='get_list_user'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='get_detail_user'),
    path('create/', views.UserCreateView.as_view(), name='post_user'),
    path('<int:pk>/update', views.UserUpdateView.as_view(), name='update_user'),
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete_user'),
    path('Z/', views.UserPublishedView.as_view(), name='get_list_user_published_true'),
]
