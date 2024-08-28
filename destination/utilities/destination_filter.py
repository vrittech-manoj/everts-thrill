import django_filters
from ..models import Destination
import ast

class DestinationFilter(django_filters.FilterSet):
    activities = django_filters.CharFilter(method='filter_by_activities')
    collections = django_filters.CharFilter(method='filter_by_collections')
    packages = django_filters.CharFilter(method='filter_by_packages')
    

    class Meta:
        model = Destination
        fields = {
            'destination_title': ['exact', 'icontains'],
            'nature_of_trip': ['exact', 'icontains'],
            'duration': ['exact','gte','lte'],
            
        }

    def filter_by_collections(self, queryset, name, value):
        try:
            collections = self.request.GET.get('collections')
            collections = collections.split(',')
            queryset = queryset.filter(collections_id__in=collections)
        except:
            pass
        return queryset
    
    
    def filter_by_activities(self, queryset, name, value):
        try:
            activities = self.request.GET.get('activities')
            activities = activities.split(',')
            queryset = queryset.filter(activities_id__in=activities)
        except:
            pass
        return queryset
    
    
    def filter_by_packages(self, queryset, name, value):
        try:
            packages = self.request.GET.get('packages')
            packages = packages.split(',')
            queryset = queryset.filter(packages_id__in=packages)
        except:
            pass
        return queryset

