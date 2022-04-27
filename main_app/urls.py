from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('fishes/', views.fishes_index, name='index'),
    path('fishes/<int:fish_id>/', views.fishes_detail, name='detail'),
    path('fishes/create/', views.FishCreate.as_view(), name='fishes_create'),
    path('fishes/<int:pk>/update/', views.FishUpdate.as_view(), name='fishes_update'),
    path('fishes/<int:pk>/delete/', views.FishDelete.as_view(), name='fishes_delete'),
    path('fishes/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('fishes/<int:fish_id>/assoc_rod/<int:rod_id>/', views.assoc_rod, name='assoc_rod'),
    path('rods/', views.RodList.as_view(), name='rods_index'),
    path('rods/<int:pk>/', views.RodDetail.as_view(), name='rods_detail'),
    path('rods/create/', views.RodCreate.as_view(), name='rods_create'),
    path('rods/<int:pk>/update/', views.RodUpdate.as_view(), name='rods_update'),
    path('rods/<int:pk>/delete/', views.RodDelete.as_view(), name='rods_delete'),
]