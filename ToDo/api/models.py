from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    complete = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.title
