from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
import csv
from destination.models import Package, Destination, DestinationGalleryImages
from review.models import Review
from collection.models import Collection
from departure.models import Departure
from booking.models import DestinationBook
from activities.models import Activity
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class GetSampleAPIView(APIView):
    """
    API view to generate and download sample data in CSV format for different models.
    """
    
    

    model_mapping = {
        "package": {
            "queryset": Package.objects.all(),
            "columns": ['name', 'image']
        },
        "destination": {
            "queryset": Destination.objects.all(),
            "columns": [
                'destination_title', 'price', 'price_type', 'is_price',
                'featured_image', 'overview', 'inclusion_and_exclusion', 'ltinerary', 'trip_map_url',
                'trip_map_image', 'gear_and_equipment', 'useful_information', 'duration', 'trip_grade',
                'best_season', 'max_altitude', 'meals', 'nature_of_trip', 'accommodation',
                'group_size'
            ]
        },
        "gallery-images": {
            "queryset": DestinationGalleryImages.objects.all(),
            "columns": [
                'id', 'destination_trip', 'image'
            ]
        },
        "review": {
            "queryset": Review.objects.all(),
            "columns": ['name', 'star_rating', 'review_description', 'add_image','is_show']
        },
        "collection": {
            "queryset": Collection.objects.all(),
            "columns": ['name', 'index', 'destination_collection']
        },
        "departure": {
            "queryset": Departure.objects.all(),
            "columns": ['destination_trip', 'upcoming_departure_date', 'upcoming_departure_status','upcoming_departure_price']
        },
        "destination-book": {
            "queryset": DestinationBook.objects.all(),
            "columns": [
                'user', 'country', 'airlines', 'number_of_travelers',
                'activity', 'package', 'arrival_date', 'departure_date', 'service_type',
                'destination', 'customize_trip'
            ]
        },
        "activity": {
            "queryset": Activity.objects.all(),
            "columns": ['name', 'image', 'destinations_activities']
        },
    }
    @swagger_auto_schema(
        operation_description="Get a sample CSV for the specified model type.",
        manual_parameters=[
            openapi.Parameter(
                'type',
                openapi.IN_PATH,
                description="Specify the type of data to fetch as CSV (e.g., 'package', 'destination').",
                type=openapi.TYPE_STRING,
                enum=list(model_mapping.keys())
            )
        ],
        responses={200: 'CSV file', 400: 'Unknown type'}
    )

    def get(self, request, type, format=None):
        model_info = self.model_mapping.get(type)

        if not model_info:
            return Response({"message": 'Unknown type'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = model_info["queryset"]
        column_list = model_info["columns"]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{type}.csv"'

        writer = csv.writer(response)

        # Write the header row
        writer.writerow(column_list)

        # Write data rows
        for data in queryset:
            data_lists = [getattr(data, column) for column in column_list]
            writer.writerow(data_lists)

        return response
