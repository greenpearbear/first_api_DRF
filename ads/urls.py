from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', views.CategoriesGETView.as_view(), name='GET_list_cat'),
    path('cat/create/', views.CategoriesPOSTView.as_view(), name='POST_cat'),
    path('ad/', views.AnnouncementsGETView.as_view(), name='GET_list_ad'),
    path('ad/create', views.AnnouncementsPOSTView.as_view(), name='POST_ad'),
    path('cat/<int:pk>/', views.CategoriesViewDetail.as_view(), name='detail_cat'),
    path('ad/<int:pk>/', views.AnnouncementsViewDetail.as_view(), name='detail_ad')
]
