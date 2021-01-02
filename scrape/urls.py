from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:part_name>/', views.view_part, name='view_part'),
]