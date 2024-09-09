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

class DepartureFilter(django_filters.FilterSet):
    """
    Custom filter for filtering Departures by the name of the month.
    Use full month names (e.g., 'January', 'February') in the 'departure_month_name' filter.
    """
    departure_month_name = filters.CharFilter(
        method='filter_by_month_name',
        label='Month Name',
        help_text='Filter by the name of the departure month. Use full month names like January, February, etc.'
    )

    class Meta:
        model = Departure
        fields = {
            'id': ['exact'],
            'upcoming_departure_date': ['exact', 'lte', 'gte'],
        }

    def filter_by_month_name(self, queryset, name, value):
        """
        Custom filter method to filter by month name.
        Validates and converts the month name to its corresponding month number.
        """
        month_number = MONTHS_MAPPING.get(value.lower())
        if month_number:
            # Filter the queryset by the month number
            return queryset.filter(upcoming_departure_date__month=month_number)
        else:
            raise ValidationError(f"Invalid month name '{value}'. Please provide a valid month name.")
