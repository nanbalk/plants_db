import django_filters

from .models import *

class PlantFilter(django_filters.FilterSet):
    class Meta:
        model = Plants
        fields = '__all__'