from django.contrib import admin
from .models import *


@admin.register(Bulletin)
class PageAdmin(admin.ModelAdmin):
    list_display = ['header',]