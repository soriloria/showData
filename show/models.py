from django.db import models


# Create your models here.

class SomeData(models.Model):
    book_name = models.CharField(max_length=100)
    book_author = models.CharField(max_length=60)
    book_pages = models.IntegerField()
