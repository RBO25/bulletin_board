from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Bulletin(models.Model):


    class Meta:
        verbose_name = 'Создать объявление'
        verbose_name_plural = 'Создать объявления'


    header = models.CharField(max_length=255, db_index=True)
    # text = models.TextField(max_length=5000, blank=True, null=True)
    text = RichTextField(max_length=5000, blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    feedback = models.ManyToManyField(User, related_name='comment', blank=True)
    reply_feedback = models.ForeignKey('self', null=True, related_name='reply_f', on_delete=models.CASCADE)


    def totalfeedback(self):
        return self.feedback.count()


    def __str__(self):
        return self.header


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
