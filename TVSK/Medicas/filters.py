import django_filters
from django_filters import CharFilter
from .models import *

class FilterAdName(django_filters.FilterSet):
    name = CharFilter(field_name='title', lookup_expr='icontains')  
    model = Doctor_Profiles
    fields ='__all__'

class FilterSpec(django_filters.FilterSet):
    spe = CharFilter(field_name='specialty', lookup_expr='icontains')  
    model = Doctor_Profiles
    fields ='__all__'
