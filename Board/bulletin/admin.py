from django.contrib import admin
from .models import *


# admin.site.register(Bulletin)
# admin.site.register(Category)
@admin.register(Bulletin)
class PageAdmin(admin.ModelAdmin):
    list_display = ['header',]