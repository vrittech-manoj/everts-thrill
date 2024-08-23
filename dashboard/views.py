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

from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class GetDashboardRequestSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=[
        ("package", "Package"),
        ("destination", "Destination"),
        ("gallery-images", "DestinationGalleryImages"),
        ("destination-review", "DestinationReview"),
        ("collection", "Collection"),
        ("departure", "Departure"),
        ("custom-user", "CustomUser"),
        ("destination-book", "DestinationBook"),
        ("activity", "Activity"),
    ], help_text="The type of model to fetch the total count for.")

class GetDashboardResponseSerializer(serializers.Serializer):
    total_count = serializers.IntegerField(help_text="The total count of records in the specified model.")

class GetDashboardAPIView(APIView):
    """
    API view to get the total count of objects in the specified model type.

    ### Available Types and Descriptions:
    - **package**: Count of all travel packages available.
    - **destination**: Count of all travel destinations listed.
    - **gallery-images**: Count of all gallery images associated with destinations.
    - **destination-review**: Count of all reviews for destinations.
    - **collection**: Count of all collections (groups of packages or destinations).
    - **departure**: Count of all departures scheduled.
    - **custom-user**: Count of all registered users.
    - **destination-book**: Count of all bookings made for destinations.
    - **activity**: Count of all activities available.
    """

    model_mapping = {
        "package": Package,
        "destination": Destination,
        "gallery-images": DestinationGalleryImages,
        "destination-review": DestinationReview,
        "collection": Collection,
        "departure": Departure,
        "destination-book": DestinationBook,
        "activity": Activity,
    }

    @swagger_auto_schema(
        operation_description="Get the total count of records for the specified model type.",
        manual_parameters=[
            openapi.Parameter(
                'type',
                openapi.IN_PATH,
                description=(
                    "Specify the type of data to fetch the total count for.\n\n"
                    "### Available Types and Descriptions:\n"
                    "- **package**: Count of all travel packages available.\n"
                    "- **destination**: Count of all travel destinations listed.\n"
                    "- **gallery-images**: Count of all gallery images associated with destinations.\n"
                    "- **destination-review**: Count of all reviews for destinations.\n"
                    "- **collection**: Count of all collections (groups of packages or destinations).\n"
                    "- **departure**: Count of all departures scheduled.\n"
                    "- **destination-book**: Count of all bookings made for destinations.\n"
                    "- **activity**: Count of all activities available."
                ),
                type=openapi.TYPE_STRING,
                enum=list(model_mapping.keys())
            )
        ],
        responses={
            200: GetDashboardResponseSerializer,
            400: 'Invalid type provided',
            500: 'Server error',
        }
    )
    def get(self, request, type, format=None):
        model = self.model_mapping.get(type)
        
        if model:
            try:
                total_count = model.objects.count()
                return Response({"total_count": total_count}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            valid_types = ", ".join(self.model_mapping.keys())
            return Response({"message": f'Unknown type. Valid types are: {valid_types}'}, status=status.HTTP_400_BAD_REQUEST)
