import django_filters
from django_filters import CharFilter
from .models import *

class FilterAdName(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')  
    model = Advisor_Profile
    fields ='__all__'

class FilterAdSpe(django_filters.FilterSet):
    specialty = CharFilter(field_name='specialty', lookup_expr='icontains')  
    model = Advisor_Profile
    fields ='__all__'



class FilterDSSP(django_filters.FilterSet):
    phanloai = CharFilter(field_name='PHANLOAI', lookup_expr='icontains')  
    model = DANH_SACH_SP
    fields ='__all__'    
