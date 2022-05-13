from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', views.CategoriesGETView.as_view(), name='GET_list_cat'),
    path('cat/create/', views.CategoriesPOSTView.as_view(), name='POST_cat'),
    path('ad/', views.AnnouncementsGETView.as_view(), name='GET_list_ad'),
    path('ad/create', views.AnnouncementsPOSTView.as_view(), name='POST_ad'),
    path('cat/<int:pk>/', views.CategoriesViewDetail.as_view(), name='detail_cat'),
    path('ad/<int:pk>/', views.AnnouncementsViewDetail.as_view(), name='detail_ad'),
    path('ad/<int:pk>/update/', views.AnnouncementsViewUpdate.as_view(), name='update_ad'),
    path('cat/<int:pk>/update/', views.CategoriesViewUpdate.as_view(), name='update_cat'),
    path('cat/<int:pk>/delete/', views.CategoriesViewDelete.as_view(), name='delete_cat'),
    path('ad/<int:pk>/delete/', views.AnnouncementsViewDelete.as_view(), name='delete_ad'),
    path('ad/<int:pk>/upload_image/', views.ImageToAd.as_view(), name='upload_image_to_ad')
]
