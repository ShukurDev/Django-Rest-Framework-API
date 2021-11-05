from django.urls import path
from . import views
urlpatterns = [
    path('listbook',views.listbooks,name='listbook')
]
