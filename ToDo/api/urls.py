from django.urls import path
from . import views

urlpatterns = [
    path('', views.overView, name='over-view'),
    path('list-task/', views.listview, name='list-task'),
    path('detail-task/<int:pk>/', views.detailview, name='detail-task'),
    path('create-task/', views.createview, name='create-taskk'),
    path('update-task/<str:pk>/', views.updateview, name='update-task'),


]
