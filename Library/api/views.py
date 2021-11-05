from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from .serializers import BookSerializers, LibUSerSerializers, RentBookSerializers, BookCategorySerializers
from .models import Book, LibUser, RentBook, BookCategory


# Create your views here.

class BookViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializers(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LibUserViewSet(viewsets.ModelViewSet):
    queryset = LibUser.objects.all()
    serializer_class = LibUSerSerializers


class RentBookViewSet(viewsets.ModelViewSet):
    queryset = RentBook.objects.all()
    serializer_class = RentBookSerializers


class BookCategoryView(generics.ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


class BookCategoryCreateView(generics.CreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


class BookCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


class BookCategoryRetrieveView(generics.RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


class BookUpdateView(generics.UpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


class BookRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers


class BookDestroyView(generics.DestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializers
