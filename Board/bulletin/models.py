from django.db import models

class Bulletin(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    # image = models.ImageField()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
