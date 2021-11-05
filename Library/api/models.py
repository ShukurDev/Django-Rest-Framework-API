from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField(null=True)

    def __str__(self):
        return self.title


class LibUser(models.Model):
    name = models.CharField(max_length=150, null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class RentBook(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(LibUser, null=True, on_delete=models.CASCADE)
    date_create = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    note = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.note


class BookCategory(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
