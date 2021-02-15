from django_filters import FilterSet,CharFilter
from .models import *
class ProductFilter(FilterSet):
    name=CharFilter(lookup_expr='icontains')
    class Meta:
        model=Product
        fields=['name','category','size']