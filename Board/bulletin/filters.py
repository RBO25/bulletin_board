from django_filters import FilterSet, CharFilter
from .models import *


class BulletinFilter(FilterSet):
    header = CharFilter(field_name='header')
    class Meta:
        model = Bulletin
        fields = '__all__'