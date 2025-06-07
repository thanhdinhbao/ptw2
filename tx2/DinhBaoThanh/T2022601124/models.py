from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
