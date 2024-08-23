import os
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from destination.models import Package, Destination, DestinationGalleryImages, DestinationReview
from booking.models import DestinationBook
from activities.models import Activity
from collection.models import Collection
from departure.models import Departure
from review.models import Review

from destination.serializers.destination_review_serializers import DestinationReviewWriteSerializers
from destination.serializers.destination_serializers import DestinationWriteSerializers
from destination.serializers.destinationgalleryimages_serializers import DestinationGalleryImagesWriteSerializers
from destination.serializers.package_serializers import PackageWriteSerializers
from review.serializers.review_serializers import ReviewWriteSerializers
from booking.serializers.destinationbook_serializers import DestinationBookWriteSerializers
from activities.serializers.activity_serializers import ActivityWriteSerializers
from collection.serializers.collection_serializers import CollectionWriteSerializers
from departure.serializers.departure_serializers import DepartureWriteSerializers

# Mapping type to model, serializer, and unique field
MODEL_MAPPING = {
    "package": {
        "model": Package,
        "serializer": PackageWriteSerializers,
        "unique_field": "name",
    },
    "destination": {
        "model": Destination,
        "serializer": DestinationWriteSerializers,
        "unique_field": "destination_title",
    },
    "gallery-images": {
        "model": DestinationGalleryImages,
        "serializer": DestinationGalleryImagesWriteSerializers,
        "unique_field": "id",
    },
    "review": {
        "model": Review,
        "serializer": ReviewWriteSerializers,
        "unique_field": "name",
    },
    "destination-book": {
        "model": DestinationBook,
        "serializer": DestinationBookWriteSerializers,
        "unique_field": "id",
    },
    "activity": {
        "model": Activity,
        "serializer": ActivityWriteSerializers,
        "unique_field": "name",
    },
    "collection": {
        "model": Collection,
        "serializer": CollectionWriteSerializers,
        "unique_field": "name",
    },
    "departure": {
        "model": Departure,
        "serializer": DepartureWriteSerializers,
        "unique_field": "id",
    },
}

VALID_TYPES = list(MODEL_MAPPING.keys())

class BulkUploadAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'excel_file': openapi.Schema(type=openapi.TYPE_FILE),
                'type': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description=f"The type of model this file belongs to. Valid types are: {', '.join(VALID_TYPES)}."
                ),
            },
            required=['excel_file', 'type']
        ),
        operation_summary="Upload Excel or CSV file with type",
        operation_description=(
            "Upload an Excel (.xlsx) or CSV (.csv) file to import data into the specified model.\n\n"
            "### Valid types:\n"
            "- `package`: For uploading packages data.\n"
            "- `destination`: For uploading destinations data.\n"
            "- `gallery-images`: For uploading destination gallery images.\n"
            "- `review`: For uploading reviews.\n"
            "- `destination-book`: For uploading destination bookings.\n"
            "- `activity`: For uploading activities data.\n"
            "- `collection`: For uploading collections.\n"
            "- `departure`: For uploading departures."
        ),
    )
    def post(self, request, format=None):
        file = request.FILES.get('excel_file')
        type = request.data.get('type', None)

        if not file or not type:
            return Response({"error": "Both 'excel_file' and 'type' are required."}, status=status.HTTP_400_BAD_REQUEST)

        file_extension = os.path.splitext(file.name)[1].lower()

        # Determine how to read the file based on its extension
        try:
            if file_extension == '.xlsx':
                df = pd.read_excel(file, engine='openpyxl')
            elif file_extension == '.csv':
                df = pd.read_csv(file)
            else:
                return Response({"error": "Unsupported file format. Only .xlsx and .csv files are allowed."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Failed to read file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the type is valid
        model_info = MODEL_MAPPING.get(type)
        if not model_info:
            return Response({"error": f"Unknown type '{type}' provided. Valid types are: {', '.join(VALID_TYPES)}."}, status=status.HTTP_400_BAD_REQUEST)

        # Convert the DataFrame to a list of dictionaries
        data_list = df.to_dict(orient='records')

        # Process the data
        try:
            create_update(
                model_info["model"],
                model_info["serializer"],
                data_list,
                model_info["unique_field"]
            )
        except Exception as e:
            return Response({"error": f"Failed to process data: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)

def create_update(my_model, my_serializer, data_list, unique_field_name):
    for record in data_list:
        existing_data = my_model.objects.filter(**{unique_field_name: record.get(unique_field_name)})
        if existing_data.exists():
            existing_instance = existing_data.first()
            serializer = my_serializer(existing_instance, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                raise ValueError("Validation error on update")
        else:
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                raise ValueError("Validation error on create")
