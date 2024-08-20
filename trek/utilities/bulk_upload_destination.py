# # from django.shortcuts import render
# # from rest_framework.response import Response
# # from rest_framework.views import APIView
# # from rest_framework import status
# # import pandas as pd
# # from urllib.parse import urlparse, parse_qs
# # from django.core.files.base import ContentFile
# # import requests
# # import logging

# # logger = logging.getLogger(__name__)

# # from drf_yasg import openapi
# # from drf_yasg.utils import swagger_auto_schema

# from destination.serializers.destination_serializers import DestinationWriteSerializers, PackageSerializers, DestinationGalleryImagesSerializer
# from destination.models import Destination, Package, DestinationGalleryImages

# # class BulkUploadAPIView(APIView):
# #     @swagger_auto_schema(
# #         request_body=openapi.Schema(
# #             type=openapi.TYPE_OBJECT,
# #             properties={
# #                 'excel_file': openapi.Schema(type=openapi.TYPE_FILE),
# #                 'packages_file': openapi.Schema(type=openapi.TYPE_FILE, required=False),
# #             },
# #             required=['excel_file']
# #         ),
# #         operation_summary="upload excel file",
# #         operation_description="upload excel file",
# #     )
# #     def post(self, request, format=None):
# #         excel_file = request.FILES.get('excel_file')
# #         packages_file = request.FILES.get('packages_file')
        
# #         if not excel_file:
# #             return Response({"error": "No excel file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
# #         try:
# #             # Use pandas to read the Excel file
# #             df = pd.read_excel(excel_file)
# #         except Exception as e:
# #             logger.error(f"Error reading excel file: {e}")
# #             return Response({"error": f"Error reading excel file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
# #         # Convert the DataFrame to a list of dictionaries
# #         data = df.to_dict(orient='records')
        
# #         for data in data:
# #             destination_serializer = DestinationWriteSerializers(data=data)
# #             if destination_serializer.is_valid():
# #                 destination = destination_serializer.save()
                
# #                 if packages_file:
# #                     try:
# #                         packages_df = pd.read_excel(packages_file)
# #                         packages_data = packages_df.to_dict(orient='records')
# #                         for package_data in packages_data:
# #                             package_serializer = PackageSerializers(data=package_data)
# #                             if package_serializer.is_valid():
# #                                 package = package_serializer.save()
# #                                 destination.packages.add(package)
# #                             else:
# #                                 logger.error(package_serializer.errors)
# #                     except Exception as e:
# #                         logger.error(f"Error processing packages file: {e}")
# #                         return Response({"error": f"Error processing packages file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
                
# #                 gallery_image_links = data.get('Gallery Images Links', '').split(',')
# #                 for link in gallery_image_links:
# #                     if link.strip():
# #                         image_file = download_image_from_google_drive(link.strip())
# #                         if image_file:
# #                             gallery_image_serializer = DestinationGalleryImagesSerializer(data={'destination_trip': destination.id, 'image': image_file})
# #                             if gallery_image_serializer.is_valid():
# #                                 gallery_image_serializer.save()
# #                             else:
# #                                 logger.error(gallery_image_serializer.errors)
# #             else:
# #                 logger.error(destination_serializer.errors)
# #                 return Response(destination_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# #         return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)

# # def download_image_from_google_drive(link):
# #     try:
# #         file_id = parse_qs(urlparse(link).query).get('id')[0]
# #         url = f"https://drive.google.com/uc?export=download&id={file_id}"
# #         response = requests.get(url)
# #         response.raise_for_status()  # Raise an exception for bad status codes
# #         return ContentFile(response.content)
# #     except requests.RequestException as e:
# #         logger.error(f"Error downloading image from Google Drive: {e}")
# #         return None
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# import pandas as pd
# from urllib.parse import urlparse, parse_qs
# from django.core.files.base import ContentFile
# import requests
# import logging

# logger = logging.getLogger(__name__)

# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema

# from destination.serializers.destination_serializers import DestinationWriteSerializers, PackageSerializers, DestinationGalleryImagesSerializer
# from destination.models import Destination, Package, DestinationGalleryImages
# class ImportExcel(APIView):
#     @swagger_auto_schema(
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'excel_file': openapi.Schema(type=openapi.TYPE_FILE),
#                 'packages_file': openapi.Schema(type=openapi.TYPE_FILE),
#             },
#             required=['excel_file']
#         ),
#         operation_summary="upload excel file",
#         operation_description="upload excel file",
#     )
#     def post(self, request, format=None):
#         excel_file = request.FILES.get('excel_file')
#         packages_file = request.FILES.get('packages_file')
        
#         if not excel_file:
#             return Response({"error": "No excel file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
#         try:
#             # Use pandas to read the Excel file
#             df = pd.read_excel(excel_file)
#         except Exception as e:
#             logger.error(f"Error reading excel file: {e}")
#             return Response({"error": f"Error reading excel file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
#         # Convert the DataFrame to a list of dictionaries
#         data = df.to_dict(orient='records')
        
#         for data in data:
#             destination_serializer = DestinationWriteSerializers(data=data)
#             if destination_serializer.is_valid():
#                 destination = destination_serializer.save()
                
#                 if packages_file:
#                     try:
#                         packages_df = pd.read_excel(packages_file)
#                         packages_data = packages_df.to_dict(orient='records')
#                         for package_data in packages_data:
#                             package_serializer = PackageSerializers(data=package_data)
#                             if package_serializer.is_valid():
#                                 package = package_serializer.save()
#                                 destination.packages.add(package)
#                             else:
#                                 logger.error(package_serializer.errors)
#                     except Exception as e:
#                         logger.error(f"Error processing packages file: {e}")
#                         return Response({"error": f"Error processing packages file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
                
#                 gallery_image_links = data.get('Gallery Images Links', '').split(',')
#                 for link in gallery_image_links:
#                     if link.strip():
#                         image_file = download_image_from_google_drive(link.strip())
#                         if image_file:
#                             gallery_image_serializer = DestinationGalleryImagesSerializer(data={'destination_trip': destination.id, 'image': image_file})
#                             if gallery_image_serializer.is_valid():
#                                 gallery_image_serializer.save()
#                             else:
#                                 logger.error(gallery_image_serializer.errors)
#             else:
#                 logger.error(destination_serializer.errors)
#                 return Response(destination_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)

# def download_image_from_google_drive(link):
#     try:
#         file_id = parse_qs(urlparse(link).query).get('id')[0]
#         url = f"https://drive.google.com/uc?export=download&id={file_id}"
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for bad status codes
#         return ContentFile(response.content)
#     except requests.RequestException as e:
#         logger.error(f"Error downloading image from Google Drive: {e}")
#         return None
