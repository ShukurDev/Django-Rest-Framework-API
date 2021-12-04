from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework import permissions
from django.contrib.auth.models import User, Group


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
