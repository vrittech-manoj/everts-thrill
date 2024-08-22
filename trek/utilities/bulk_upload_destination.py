from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import requests
from django.core.files.base import ContentFile
from django.db import transaction
import json
import logging

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from destination.models import Destination, DestinationGalleryImages, Package
from destination.serializers.destination_serializers import DestinationWriteSerializers

logger = logging.getLogger(__name__)

class BulkUploadAPIView(APIView):
    pass
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'excel_file': openapi.Schema(type=openapi.TYPE_FILE),
            },
            required=['excel_file']
        ),
        operation_summary="Upload Excel file for destination data",
        operation_description="Upload Excel file containing destination data",
    )
    def post(self, request, format=None):
        file = request.FILES.get('excel_file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Use pandas to read the Excel file
        try:
            df = pd.read_excel(file)
        except Exception as e:
            return Response({"error": f"Failed to read Excel file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Convert the DataFrame to a list of dictionaries
        datas = df.to_dict(orient='records')
        
        try:
            create_update_destination(Destination, DestinationWriteSerializers, datas)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)


def create_update_destination(my_model, my_serializer, datas):
    for record in datas:
        # Handle image links (featured image)
        image_link = record.get('Featured Image Link')
        if image_link:
            try:
                response = requests.get(image_link)
                if response.status_code == 200:
                    record['featured_image'] = ContentFile(response.content, name=f"{record.get('destination_title')}_featured.jpg")
                else:
                    record['featured_image'] = None
            except Exception as e:
                record['featured_image'] = None

        # Handle packages
        package_names = record.get('Packages')
        if package_names:
            package_names_list = json.loads(package_names)
            packages = Package.objects.filter(name__in=package_names_list)
            if packages.exists():
                record['packages'] = [package.id for package in packages]
            else:
                record['packages'] = []

        # Check if the destination already exists
        existing_data = my_model.objects.filter(destination_title=record['destination_title'])
        if existing_data.exists():
            # Update existing record
            existing_data = existing_data.first()
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Validation errors for record {record['destination_title']}: {serializer.errors}")
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(f"Validation errors for new record {record['destination_title']}: {serializer.errors}")
                # Handle validation errors
                pass
