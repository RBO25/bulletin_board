from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Bulletin(models.Model):

    TANKI = 'TK'
    HILL = 'HL'
    DD = 'DD'
    TORG = 'TG'
    GILD = 'CM'
    KWEST = 'KW'
    KUZN = 'KZ'
    KOZH = 'KZH'
    ZELL = 'ZL'
    MASTERS = 'MT'
    CATEGORY_CHOICES = [
        (TANKI, 'Танки'),
        (HILL, 'Хилы'),
        (DD, 'ДД'),
        (TORG, 'Торговцы'),
        (GILD, 'Гилдмастеры'),
        (KWEST, 'Квестгиверы'),
        (KUZN, 'Кузнецы'),
        (KOZH, 'Кожевники'),
        (ZELL, 'Зельевары'),
        (MASTERS, 'Мастера заклинаний'),
    ]

    class Meta:
        verbose_name = 'Создать объявление'
        verbose_name_plural = 'Создать объявления'


    header = models.CharField(max_length=255, db_index=True)
    text = RichTextField(max_length=5000, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    feedback = models.ManyToManyField(User, max_length=255, related_name='comment', blank=True)
    # reply_feedback = models.ForeignKey('self', null=True, related_name='reply_f', on_delete=models.CASCADE)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=TANKI)


    def totalfeedback(self):
        return self.feedback.count()


    def get_absolute_url(self):
        return reverse('bulletin', args=[str(self.id)])


    def __str__(self):
        return self.header


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2", )