from django.urls import path
from . import views


urlpatterns = [
    path('cat/', views.CategoriesListView.as_view(), name='GET_list_cat'),
    path('cat/create/', views.CategoriesCreateView.as_view(), name='POST_cat'),
    path('ad/', views.AnnouncementsListView.as_view(), name='GET_list_ad'),
    path('ad/create', views.AnnouncementsCreateView.as_view(), name='POST_ad'),
    path('cat/<int:pk>/', views.CategoriesDetailView.as_view(), name='detail_cat'),
    path('ad/<int:pk>/', views.AnnouncementsDetailView.as_view(), name='detail_ad'),
    path('ad/<int:pk>/update/', views.AnnouncementsUpdateView.as_view(), name='update_ad'),
    path('cat/<int:pk>/update/', views.CategoriesUpdateView.as_view(), name='update_cat'),
    path('cat/<int:pk>/delete/', views.CategoriesDeleteView.as_view(), name='delete_cat'),
    path('ad/<int:pk>/delete/', views.AnnouncementsDeleteView.as_view(), name='delete_ad'),
    path('ad/<int:pk>/upload_image/', views.ImageToAd.as_view(), name='upload_image_to_ad'),
]
