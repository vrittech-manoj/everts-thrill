from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from destination.models import Package, Destination, DestinationGalleryImages, DestinationReview
from collection.models import Collection
from departure.models import Departure
from accounts.models import CustomUser
from booking.models import DestinationBook
from activities.models import Activity
from queries.models import Queries

from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class GetAllCountsResponseSerializer(serializers.Serializer):
    package = serializers.IntegerField(help_text="Total count of travel packages available", required=False)
    destination = serializers.IntegerField(help_text="Total count of travel destinations listed", required=False)
    gallery_images = serializers.IntegerField(help_text="Total count of gallery images associated with destinations", required=False)
    destination_review = serializers.IntegerField(help_text="Total count of reviews for destinations", required=False)
    collection = serializers.IntegerField(help_text="Total count of collections", required=False)
    departure = serializers.IntegerField(help_text="Total count of departures scheduled", required=False)
    custom_user = serializers.IntegerField(help_text="Total count of registered users", required=False)
    destination_book = serializers.IntegerField(help_text="Total count of bookings made for destinations", required=False)
    activity = serializers.IntegerField(help_text="Total count of activities available", required=False)
    queries = serializers.IntegerField(help_text="Total count of activities available", required=False)

class GetDashboardAPIView(APIView):
    """
    API view to retrieve the total count of records for key models in the system.

    Models included:
    - package
    - destination
    - gallery_images
    - destination_review
    - collection
    - departure
    - custom_user
    - destination_book
    - activity
    - queries
    """

    model_mapping = {
        "package": Package,
        "destination": Destination,
        "gallery_images": DestinationGalleryImages,
        "destination_review": DestinationReview,
        "collection": Collection,
        "departure": Departure,
        "custom_user": CustomUser,
        "destination_book": DestinationBook,
        "activity": Activity,
        "queries": Queries
    }

    @swagger_auto_schema(
        operation_description="Retrieve total counts of records for all specified models.",
        responses={
            200: openapi.Response(
                description="Total count of records for each model",
                schema=GetAllCountsResponseSerializer
            ),
            500: openapi.Response(
                description="Server error."
            )
        }
    )
    def get(self, request, format=None):
        counts = {}
        try:
            for key, model in self.model_mapping.items():
                counts[key] = model.objects.count()
            return Response(counts, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)