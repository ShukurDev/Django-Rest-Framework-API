from django.urls import path
from rest_framework.urls import urlpatterns
from . import views
from api.views import viewsets

urlpatterns += {
    path('list-view/', views.BookCategoryView.as_view()),
    path('create-view',views.BookCategoryCreateView.as_view()),
    path('list-create-view/', views.BookCategoryListCreateView.as_view()),
    path('retrieve-view/<int:pk>/',views.BookCategoryRetrieveView.as_view()),
    path('update-view/<int:pk>/',views.BookUpdateView.as_view()),
    path('retrieve-update-view/<int:pk>/', views.BookRetrieveUpdateView.as_view()),
    path('destroy-view/<int:pk>/',views.BookDestroyView.as_view()),
}
