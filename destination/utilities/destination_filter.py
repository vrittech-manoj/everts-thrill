import django_filters
from ..models import Destination

class DestinationFilter(django_filters.FilterSet):
    activities = django_filters.CharFilter(method='filter_by_activities')
    collections = django_filters.CharFilter(method='filter_by_collections')
    packages = django_filters.CharFilter(method='filter_by_packages')

    class Meta:
        model = Destination
        fields = {
            'destination_title': ['exact', 'icontains'],
            'nature_of_trip': ['exact', 'icontains'],
            'duration': ['exact', 'gte', 'lte'],
        }

    def filter_by_collections(self, queryset, name, value):
        if value:
            collections = value.split(',') if ',' in value else [value]
            queryset = queryset.filter(collections__id__in=collections)
        return queryset

    def filter_by_activities(self, queryset, name, value):
        if value:
            activities = value.split(',') if ',' in value else [value]
            queryset = queryset.filter(activities__id__in=activities)
        return queryset

    def filter_by_packages(self, queryset, name, value):
        if value:
            packages = value.split(',') if ',' in value else [value]
            queryset = queryset.filter(packages__id__in=packages)
        return queryset
