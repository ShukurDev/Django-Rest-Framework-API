from rest_framework import serializers
from .models import Book, LibUser, RentBook, BookCategory


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class LibUSerSerializers(serializers.ModelSerializer):
    class Meta:
        model = LibUser
        fields = '__all__'


class RentBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = RentBook
        fields = '__all__'


class BookCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BookCategory
        fields = '__all__'
