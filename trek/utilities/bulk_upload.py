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
            create_update_packages(Package, PackageWriteSerializers, datas, 'name', type)
        elif type == "destination":
            create_update_destinations(Destination, DestinationWriteSerializers, datas, 'destination_title', type)
        elif type == "destination-gallery-images":
            create_update_gallery_images(DestinationGalleryImages, DestinationGalleryImagesWriteSerializers, datas, 'id', type)
        elif type == "destination-book":
            create_update_destination_book(DestinationBook, DestinationBookWriteSerializers, datas, 'user__email', type)
        elif type == "activity":
            create_update_activities(Activity, ActivityWriteSerializers, datas, 'name', type)
        elif type == "collection":
            create_update_collections(Collection, CollectionWriteSerializers, datas, 'name', type)
        elif type == "departure":
            create_update_departures(Departure, DepartureWriteSerializers, datas, 'id', type)
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

def create_update_packages(my_model, my_serializer, datas, unique_field_name):
    
    for record in datas:
        existing_data = my_model.objects.filter(name=record[unique_field_name])
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass
def create_update_gallery_images(my_model, my_serializer, datas, unique_field_name):
    
    for record in datas:
        # Resolve the foreign key if it's provided as a name or identifier
        if isinstance(record[unique_field_name], str):
            destination_obj = Destination.objects.filter(name=record[unique_field_name]).first()
        elif isinstance(record[unique_field_name], int):
            destination_obj = Destination.objects.filter(id=record[unique_field_name]).first()
        else:
            destination_obj = record[unique_field_name]  # Assume it's already a Destination instance

        if not destination_obj:
            # Handle the case where the foreign key is not found
            continue
        
        record['destination_trip'] = destination_obj.id  # Ensure you're using the foreign key ID

        existing_data = my_model.objects.filter(destination_trip=destination_obj)

        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass

def create_update_destination_book(my_model, my_serializer, datas, unique_field_name):
    
    for record in datas:
        # Resolve or create the foreign keys if provided as names or identifiers
        if 'activity' in record:
            if isinstance(record['activity'], str):
                activity_obj, created = Activity.objects.get_or_create(name=record['activity'])
            elif isinstance(record['activity'], int):
                activity_obj = Activity.objects.filter(id=record['activity']).first()
            else:
                activity_obj = record['activity']  # Assume it's already an Activity instance

            if not activity_obj:
                # If still not found, skip the record
                continue
            
            record['activity'] = activity_obj.id  # Ensure you're using the foreign key ID

        if 'package' in record:
            if isinstance(record['package'], str):
                package_obj, created = Package.objects.get_or_create(name=record['package'])
            elif isinstance(record['package'], int):
                package_obj = Package.objects.filter(id=record['package']).first()
            else:
                package_obj = record['package']  # Assume it's already a Package instance

            if not package_obj:
                # If still not found, skip the record
                continue
            
            record['package'] = package_obj.id  # Ensure you're using the foreign key ID

        if 'destination' in record:
            if isinstance(record['destination'], str):
                destination_obj, created = Destination.objects.get_or_create(title=record['destination'])
            elif isinstance(record['destination'], int):
                destination_obj = Destination.objects.filter(id=record['destination']).first()
            else:
                destination_obj = record['destination']  # Assume it's already a Destination instance

            if not destination_obj:
                # If still not found, skip the record
                continue
            
            record['destination'] = destination_obj.id  # Ensure you're using the foreign key ID

        existing_data = my_model.objects.filter(**{unique_field_name: record[unique_field_name]})
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass

def create_update_activities(my_model, my_serializer, datas, unique_field_name):
    
    for record in datas:
        # Resolve or create the ManyToMany field (destinations_activities)
        if 'destinations_activities' in record:
            destination_ids = []
            for destination_name in record['destinations_activities']:
                if isinstance(destination_name, str):
                    destination_obj, created = Destination.objects.get_or_create(title=destination_name)
                elif isinstance(destination_name, int):
                    destination_obj = Destination.objects.filter(id=destination_name).first()
                else:
                    destination_obj = destination_name  # Assume it's already a Destination instance

                if destination_obj:
                    destination_ids.append(destination_obj.id)

            # Replace the destination names/instances with their IDs in the record
            record['destinations_activities'] = destination_ids

        existing_data = my_model.objects.filter(name=record[unique_field_name])
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                activity = serializer.save()
                if 'destinations_activities' in record:
                    activity.destinations_activities.set(record['destinations_activities'])  # Update the ManyToMany field
            else:
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                activity = serializer.save()
                if 'destinations_activities' in record:
                    activity.destinations_activities.set(record['destinations_activities'])  # Set the ManyToMany field
            else:
                # Handle validation errors
                pass

def create_update_collections(my_model, my_serializer, datas, unique_field_name):
    
    for record in datas:
        # Resolve or create the ManyToMany field (destination_collection)
        if 'destination_collection' in record:
            destination_ids = []
            for destination_name in record['destination_collection']:
                if isinstance(destination_name, str):
                    destination_obj, created = Destination.objects.get_or_create(title=destination_name)
                elif isinstance(destination_name, int):
                    destination_obj = Destination.objects.filter(id=destination_name).first()
                else:
                    destination_obj = destination_name  # Assume it's already a Destination instance

                if destination_obj:
                    destination_ids.append(destination_obj.id)

            # Replace the destination names/instances with their IDs in the record
            record['destination_collection'] = destination_ids

        existing_data = my_model.objects.filter(name=record[unique_field_name])
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                collection = serializer.save()
                if 'destination_collection' in record:
                    collection.destination_collection.set(record['destination_collection'])  # Update the ManyToMany field
            else:
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                collection = serializer.save()
                if 'destination_collection' in record:
                    collection.destination_collection.set(record['destination_collection'])  # Set the ManyToMany field
            else:
                # Handle validation errors
                pass

def create_update_departures(my_model, my_serializer, datas, unique_field_name):
    
    for record in datas:
        # Resolve or create the ForeignKey field (destination_trip)
        if 'destination_trip' in record:
            if isinstance(record['destination_trip'], str):
                destination_obj, created = Destination.objects.get_or_create(title=record['destination_trip'])
            elif isinstance(record['destination_trip'], int):
                destination_obj = Destination.objects.filter(id=record['destination_trip']).first()
            else:
                destination_obj = record['destination_trip']  # Assume it's already a Destination instance

            if not destination_obj:
                # If the destination is not found, skip the record
                continue
            
            record['destination_trip'] = destination_obj.id  # Ensure you're using the foreign key ID

        existing_data = my_model.objects.filter(**{unique_field_name: record[unique_field_name]})
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                # Handle validation errors
                pass

def create_update_destinations(my_model, my_serializer, datas, unique_field_name):
    
    for record in datas:
        # Resolve or create the ManyToMany field (packages)
        if 'packages' in record:
            package_ids = []
            for package_name in record['packages']:
                if isinstance(package_name, str):
                    package_obj, created = Package.objects.get_or_create(name=package_name)
                elif isinstance(package_name, int):
                    package_obj = Package.objects.filter(id=package_name).first()
                else:
                    package_obj = package_name  # Assume it's already a Package instance

                if package_obj:
                    package_ids.append(package_obj.id)

            # Replace the package names/instances with their IDs in the record
            record['packages'] = package_ids

        # Handling other fields and creating or updating the Destination record
        existing_data = my_model.objects.filter(destination_title=record[unique_field_name])
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                destination = serializer.save()
                if 'packages' in record:
                    destination.packages.set(record['packages'])  # Update the ManyToMany field
            else:
                # Handle validation errors
                pass
        else:
            # Create a new record
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                destination = serializer.save()
                if 'packages' in record:
                    destination.packages.set(record['packages'])  # Set the ManyToMany field
            else:
                # Handle validation errors
                pass
