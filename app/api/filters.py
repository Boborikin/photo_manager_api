import django_filters
from django_filters import DateTimeFilter, CharFilter
from .models import Photo


class CustomPhotoFilter(django_filters.FilterSet):
    upload_date = DateTimeFilter(field_name='upload_date', lookup_expr='exact')
    upload_date_gte = DateTimeFilter(field_name='upload_date', lookup_expr='gte')
    upload_date_lte = DateTimeFilter(field_name='upload_date', lookup_expr='lte')
    upload_date_gt = DateTimeFilter(field_name='upload_date', lookup_expr='gt')
    upload_date_lt = DateTimeFilter(field_name='upload_date', lookup_expr='lt')

    people_list = CharFilter(lookup_expr='icontains')

    geolocation = CharFilter(lookup_expr='icontains')


    class Meta:
        model = Photo
        fields = ("upload_date", 'people_list')


