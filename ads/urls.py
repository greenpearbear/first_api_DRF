from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', views.CategoriesView.as_view(), name='POST_and_GET_categories'),
    path('ad/', views.AnnouncementsView.as_view(), name='POST_and_GET_announcement'),
    path('cat/<int:pk>/', views.CategoriesViewDetail.as_view(), name='detail_cat'),
    path('ad/<int:pk>/', views.AnnouncementsViewDetail.as_view(), name='detail_ad')
]
