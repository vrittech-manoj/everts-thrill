import django_filters
import re
from django.db.models import Q
from ..models import Destination
import django_filters
from django_filters import rest_framework as filters
from ..models import Departure
from rest_framework.exceptions import ValidationError


# Mapping month names to their corresponding numbers
MONTHS_MAPPING = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4,
    'may': 5, 'june': 6, 'july': 7, 'august': 8,
    'september': 9, 'october': 10, 'november': 11, 'december': 12
}

class DestinationFilter(django_filters.FilterSet):
    activities = django_filters.CharFilter(method='filter_by_activities')
    collections = django_filters.CharFilter(method='filter_by_collections')
    packages = django_filters.CharFilter(method='filter_by_packages')
    departure_month_name = django_filters.CharFilter(
        method='filter_by_departure_month_name',
        label='Departure Month (Name)',
        help_text='Filter by the name of the departure month. Use full month names like January, February, etc.'
    )
    duration_gte = django_filters.NumberFilter(label='Duration (Greater than or equal to)', method='filter_by_duration_gte')
    duration_lte = django_filters.NumberFilter(label='Duration (Less than or equal to)', method='filter_by_duration_lte')

    class Meta:
        model = Destination
        fields = {
            'destination_title': ['exact', 'icontains'],
            'nature_of_trip': ['exact', 'icontains'],
            'accommodation': ['exact', 'icontains'],
            'created_date': ['exact', 'gte', 'lte'],
            'best_season': ['exact', 'icontains'],
            'trip_grade': ['exact', 'icontains'],
            'price': ['exact'],
            'trip_grade': ['exact'],
            'max_altitude': ['exact'],
            'best_season': ['exact'],
        }
# ('public_id', 'slug', 'destination_title', 'packages', 'price', 'price_type', 'is_price', 'featured_image', 'overview', 'inclusion_and_exclusion', 'ltinerary', 'trip_map_url', 'trip_map_image', 'gear_and_equipment', 'useful_information', 'duration', 'trip_grade', 'best_season', 'max_altitude', 'meals', 'nature_of_trip', 'accommodation', 'group_size', )
    def filter_by_collections(self, queryset, name, value):
        if value:
            collections = value.split(',') if ',' in value else [value]
            queryset = queryset.filter(collections__id__in=collections)
        return queryset

    def filter_by_packages(self, queryset, name, value):
        if value:
            packages = value.split(',') if ',' in value else [value]
            queryset = queryset.filter(packages__id__in=packages)
        return queryset

    def filter_by_activities(self, queryset, name, value):
        if value:
            activities = value.split(',') if ',' in value else [value]
            queryset = queryset.filter(activities__id__in=activities).distinct()
        return queryset

    def extract_min_max_duration(self, duration_str):
        """
        Extracts the minimum and maximum duration from the duration string.
        Example: "5-10 Days" -> (5, 10), "7 Days" -> (7, 7)
        """
        numbers = re.findall(r'\d+', duration_str)
        if len(numbers) == 1:
            return int(numbers[0]), int(numbers[0])
        elif len(numbers) == 2:
            return int(numbers[0]), int(numbers[1])
        return None, None

    def filter_by_duration_gte(self, queryset, name, value):
        """
        Custom method to handle gte (greater than or equal to) duration filtering.
        """
        if value is not None:
            return queryset.filter(id__in=[
                obj.id for obj in queryset
                if self.extract_min_max_duration(obj.duration)[1] >= value
            ])
        return queryset

    def filter_by_duration_lte(self, queryset, name, value):
        """
        Custom method to handle lte (less than or equal to) duration filtering.
        """
        if value is not None:
            return queryset.filter(id__in=[
                obj.id for obj in queryset
                if self.extract_min_max_duration(obj.duration)[0] <= value
            ])
        return queryset

    def filter_queryset(self, queryset):
        """
        Override the filter_queryset method to handle both gte and lte filters together.
        """
        queryset = super().filter_queryset(queryset)

        # Custom duration range handling
        duration_gte = self.data.get('duration_gte')
        duration_lte = self.data.get('duration_lte')

        if duration_gte and duration_lte:
            try:
                gte_value = int(duration_gte)
                lte_value = int(duration_lte)
                return self.filter_by_duration_gte(self.filter_by_duration_lte(queryset, None, lte_value), None, gte_value)
            except ValueError:
                pass  # Ignore invalid values and don't filter

        return queryset
    
    def filter_by_departure_month_name(self, queryset, name, value):
        """
        Custom filter method to filter Destinations by the month name of upcoming departures.
        Converts the month name to its corresponding month number.
        """
        month_number = MONTHS_MAPPING.get(value.lower())
        if month_number:
            # Filter destinations where associated departures have upcoming_departure_date in the specified month
            return queryset.filter(destination_departures__upcoming_departure_date__month=month_number)
        else:
            raise ValidationError(f"Invalid month name '{value}'. Please provide a valid month name.")
