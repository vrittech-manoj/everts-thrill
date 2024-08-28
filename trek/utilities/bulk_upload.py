from django.shortcuts import render
from django.http import HttpResponse
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

# Create your views here.

class BulkUploadAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'excel_file': openapi.Schema(type=openapi.TYPE_FILE),
                'type': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Specify the type of data to import. Options are: 'package', 'destination', 'destination-gallery-images', 'destination-review', 'destination-book', 'activity', 'collection', 'departure', 'review'.",
                    enum=[
                        'package',
                        'destination',
                        'destination-gallery-images',
                        'destination-review',
                        'destination-book',
                        'activity',
                        'collection',
                        'departure',
                        'review'
                    ]
                ),
            },
            required=['excel_file', 'type']
        ),
        operation_summary="Upload Excel file",
        operation_description="Upload an Excel file and import data into the specified model based on the provided type.",
    )
    def post(self, request, format=None):
        file = request.FILES.get('excel_file')
        type = request.data.get('type')

        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        if not type:
            return Response({"error": "No type provided"}, status=status.HTTP_400_BAD_REQUEST)

        df = pd.read_csv(file)
        datas = df.to_dict(orient='records')

        if type == "package":
            create_update_records(Package, PackageWriteSerializers, datas, 'name', type)
        elif type == "destination":
            create_update_records(Destination, DestinationWriteSerializers, datas, 'destination_title', type)
        elif type == "destination-gallery-images":
            create_update_records(DestinationGalleryImages, DestinationGalleryImagesWriteSerializers, datas, 'id', type)
        elif type == "destination-book":
            create_update_records(DestinationBook, DestinationBookWriteSerializers, datas, 'user__email', type)
        elif type == "activity":
            create_update_records(Activity, ActivityWriteSerializers, datas, 'name', type)
        elif type == "collection":
            create_update_records(Collection, CollectionWriteSerializers, datas, 'name', type)
        elif type == "departure":
            create_update_records(Departure, DepartureWriteSerializers, datas, 'id', type)
        elif type == "review":
            create_update(Review, ReviewWriteSerializers, datas, 'name', type)
        else:
            return Response({"message": "Unknown file type"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)


def create_update(my_model,my_serializer,datas,unique_field_name):
    
    for record in datas:
        existing_data = my_model.objects.filter(**{unique_field_name: record[unique_field_name]})
        if existing_data.exists():
            existing_data = existing_data.first()  # Use a unique field here
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
                pass


def create_update_records(my_model, my_serializer, datas, unique_field_name, related_fields=None):
    if related_fields is None:
        related_fields = {}

    for record in datas:
        # Process related fields if any
        for field, relation in related_fields.items():
            if field in record:
                related_model = relation['model']
                lookup_field = relation['lookup_field']
                related_obj = related_model.objects.filter(**{lookup_field: record[field]}).first()
                if related_obj:
                    record[field] = related_obj.id
                else:
                    print(f"Related instance for {field} with value '{record[field]}' not found.")
                    continue

        # Find existing data
        existing_data = my_model.objects.filter(**{unique_field_name: record[unique_field_name]}).first()

        if existing_data:
            # Update existing record
            serializer = my_serializer(existing_data, data=record)
        else:
            # Create a new record
            serializer = my_serializer(data=record)

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)  # Handle validation errors
