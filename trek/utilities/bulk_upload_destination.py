from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import requests
from django.core.files.base import ContentFile
from django.db import transaction
import json

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from destination.models import Destination, DestinationGalleryImages, Package
from destination.serializers.destination_serializers import DestinationWriteSerializers

class BulkUploadAPIView(APIView):
    """
    API view to handle bulk upload of destination data from an Excel file.
    """
    @swagger_auto_schema(
        operation_description="Bulk upload destination data from an Excel file",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'excel_file': openapi.Schema(type=openapi.TYPE_FILE, description='Excel file containing destination data'),
            },
            required=['excel_file']
        ),
        responses={201: 'Bulk upload successful', 400: 'Error in processing'}
    )
   
    def post(self, request, *args, **kwargs):
        # Get the uploaded Excel file
        excel_file = request.FILES.get('excel_file')
        if not excel_file:
            return Response({"error": "No Excel file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Read the Excel file into a DataFrame
            df = pd.read_excel(excel_file)
        except Exception as e:
            return Response({"error": f"Failed to read Excel file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Convert the DataFrame to a list of dictionaries
        records = df.to_dict(orient='records')

        with transaction.atomic():
            for record in records:
                try:
                    # Handle featured image from public Google Drive link
                    image_link = record.get('Featured Image Link')
                    if image_link:
                        response = requests.get(image_link)
                        if response.status_code == 200:
                            record['featured_image'] = ContentFile(response.content, name=f"{record.get('Destination Title')}_featured.jpg")
                        else:
                            print(f"Failed to download featured image: {image_link}")

                    # Handle packages: Expecting a list of package names
                    package_names = record.get('Packages')
                    if package_names:
                        package_names_list = json.loads(package_names)
                        packages = Package.objects.filter(name__in=package_names_list)
                        if packages.exists():
                            record['packages'] = [package.id for package in packages]
                        else:
                            return Response({"error": f"One or more packages not found: {package_names_list}"}, status=status.HTTP_400_BAD_REQUEST)

                    # Directly pass the record to the serializer
                    serializer = DestinationWriteSerializers(data=record)
                    if serializer.is_valid():
                        destination_instance = serializer.save()

                        # Handle gallery images
                        gallery_image_links = record.get('Gallery Image Links')
                        if gallery_image_links:
                            gallery_images = json.loads(gallery_image_links)
                            for image_url in gallery_images:
                                response = requests.get(image_url)
                                if response.status_code == 200:
                                    image_content = ContentFile(response.content, name=f"{destination_instance.destination_title}_gallery.jpg")
                                    DestinationGalleryImages.objects.create(destination_trip=destination_instance, image=image_content)
                                else:
                                    print(f"Failed to download gallery image: {image_url}")
                    else:
                        print(serializer.errors)
                        continue

                except Exception as e:
                    return Response({"error": f"Error processing record: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Bulk upload successful"}, status=status.HTTP_201_CREATED)
