from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
import json

import os
import requests
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

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
        operation_summary="Upload CSV or Excel file",
        operation_description="Upload a CSV or Excel file and import data into the specified model based on the provided type.",
    )
    def post(self, request, format=None):
        file = request.FILES.get('excel_file')
        data_type = request.data.get('type')

        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        if not data_type:
            return Response({"error": "No type provided"}, status=status.HTTP_400_BAD_REQUEST)

        file_name = file.name
        if file_name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file_name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            return Response({"error": "Unsupported file type. Only .csv, .xls, and .xlsx files are supported."}, status=status.HTTP_400_BAD_REQUEST)

        data = df.to_dict(orient='records')

        if data_type == "package":
            create_update_packages(Package, PackageWriteSerializers, data, 'name')
        elif data_type == "destination":
            create_update_destinations(Destination, DestinationWriteSerializers, data, 'destination_title', request)
        elif data_type == "destination-gallery-images":
            create_update_gallery_images(DestinationGalleryImages, DestinationGalleryImagesWriteSerializers, data, 'id')
        elif data_type == "destination-book":
            create_update_destination_book(DestinationBook, DestinationBookWriteSerializers, data, 'email')
        elif data_type == "activity":
            create_update_activities(Activity, ActivityWriteSerializers, data, 'name')
        elif data_type == "collection":
            create_update_collections(Collection, CollectionWriteSerializers, data, 'name')
        elif data_type == "departure":
            create_update_departures(Departure, DepartureWriteSerializers, data, 'upcoming_departure_date')
        elif data_type == "review":
            create_update(Review, ReviewWriteSerializers, data, 'name')
        else:
            return Response({"message": "Unknown file type"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "File processed successfully"}, status=status.HTTP_201_CREATED)

def create_update(my_model,my_serializer,data,unique_field_name):
    
    for record in data:
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

def create_update_packages(my_model, my_serializer, data, unique_field_name):
    
    for record in data:
        existing_data = my_model.objects.filter(name=record[unique_field_name])
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
        else:
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors

def create_update_gallery_images(my_model, my_serializer, data, unique_field_name):
    
    for record in data:
        # Resolve the ForeignKey field (destination_trip)
        if 'destination_trip' in record:
            if isinstance(record['destination_trip'], str):
                destination_obj = Destination.objects.filter(destination_title=record['destination_trip']).first()
            elif isinstance(record['destination_trip'], int):
                destination_obj = Destination.objects.filter(id=record['destination_trip']).first()
            else:
                destination_obj = record['destination_trip']  # Assume it's already a Destination instance

            if not destination_obj:
                raise ValueError(f"Destination with title '{record['destination_trip']}' does not exist.")
            
            record['destination_trip'] = destination_obj.id  # Ensure you're using the foreign key ID

        existing_data = my_model.objects.filter(destination_trip=destination_obj)

        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
        else:
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors


def create_update_destination_book(my_model, my_serializer, data, unique_field_name):
    
    for record in data:
        # Resolve the foreign keys, and throw an error if not found
        if 'activity' in record:
            if isinstance(record['activity'], str):
                activity_obj = Activity.objects.filter(name=record['activity']).first()
            elif isinstance(record['activity'], int):
                activity_obj = Activity.objects.filter(id=record['activity']).first()
            else:
                activity_obj = record['activity']  # Assume it's already an Activity instance

            if not activity_obj:
                raise ValueError(f"Activity with name '{record['activity']}' does not exist.")
            record['activity'] = activity_obj.id  # Ensure you're using the foreign key ID

        if 'package' in record:
            if isinstance(record['package'], str):
                package_obj = Package.objects.filter(name=record['package']).first()
            elif isinstance(record['package'], int):
                package_obj = Package.objects.filter(id=record['package']).first()
            else:
                package_obj = record['package']  # Assume it's already a Package instance

            if not package_obj:
                raise ValueError(f"Package with name '{record['package']}' does not exist.")
            record['package'] = package_obj.id  # Ensure you're using the foreign key ID

        if 'destination' in record:
            if isinstance(record['destination'], str):
                destination_obj = Destination.objects.filter(destination_title=record['destination']).first()
            elif isinstance(record['destination'], int):
                destination_obj = Destination.objects.filter(id=record['destination']).first()
            else:
                destination_obj = record['destination']  # Assume it's already a Destination instance

            if not destination_obj:
                raise ValueError(f"Destination with title '{record['destination']}' does not exist.")
            record['destination'] = destination_obj.id  # Ensure you're using the foreign key ID

        existing_data = my_model.objects.filter(**{unique_field_name: record[unique_field_name]})
        
        if existing_data.exists():
            existing_data = existing_data.first()  # Get the existing record based on the unique field
            
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors
        else:
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)
                # Handle validation errors


import os
import requests
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File

def create_update_activities(my_model, my_serializer, data, unique_field_name):
    errors = []
    missing_destinations = []

    for record in data:
        # Handle image if it's provided as a URL, or set to None if you want to ignore it
        if 'image' in record:
            record['image'] = None

        # Process destinations_activities_names, splitting by comma
        if 'destinations_activities_names' in record:
            destination_names_str = record['destinations_activities_names']
            # Split by commas and strip any surrounding whitespace
            destination_names = [name.strip() for name in destination_names_str.split(',')]

            destination_ids = []
            for destination_name in destination_names:
                destination_obj = Destination.objects.filter(destination_title=destination_name).first()
                if not destination_obj:
                    missing_destinations.append(destination_name)
                else:
                    destination_ids.append(destination_obj.id)

            if not destination_ids:
                errors.append(f"No valid destinations found in 'destinations_activities_names' for record with {unique_field_name}='{record[unique_field_name]}'.")
                continue

            record['destinations_activities'] = destination_ids
        else:
            errors.append(f"destinations_activities_names field is required in record with {unique_field_name}='{record[unique_field_name]}'.")
            continue

        existing_data = my_model.objects.filter(name=record[unique_field_name])
        
        if existing_data.exists():
            existing_data = existing_data.first()
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                activity = serializer.save()
                if 'destinations_activities' in record:
                    activity.destinations_activities.set(record['destinations_activities'])
            else:
                errors.append(f"Validation error in record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")
        else:
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                activity = serializer.save()
                if 'destinations_activities' in record:
                    activity.destinations_activities.set(record['destinations_activities'])
            else:
                errors.append(f"Validation error in new record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")

    if missing_destinations:
        raise ValueError(f"Destinations with the following titles do not exist: {', '.join(missing_destinations)}")

    if errors:
        raise ValueError("Errors occurred during processing:\n" + "\n".join(errors))


def create_update_collections(my_model, my_serializer, data, unique_field_name):
    errors = []
    missing_destinations = []

    for record in data:
        # Ensure that destination_collection is treated as a list of complete titles
        if 'destination_collection' in record:
            destination_names = record['destination_collection']

            # Ensure destination_names is treated as a list
            if isinstance(destination_names, str):
                destination_names = [destination_names]  # Convert to a list if it's a single string
            elif not isinstance(destination_names, list):
                errors.append(f"Invalid format for destination_collection in record with {unique_field_name}='{record[unique_field_name]}'. Expected a list or string.")
                continue

            destination_ids = []
            for destination_name in destination_names:
                destination_obj = Destination.objects.filter(destination_title=destination_name).first()

                if not destination_obj:
                    missing_destinations.append(destination_name)
                else:
                    destination_ids.append(destination_obj.id)

            record['destination_collection'] = destination_ids

        if missing_destinations:
            continue

        existing_data = my_model.objects.filter(name=record[unique_field_name])
        
        if existing_data.exists():
            existing_data = existing_data.first()
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                collection = serializer.save()
                if 'destination_collection' in record:
                    collection.destination_collection.set(record['destination_collection'])
            else:
                errors.append(f"Validation error in record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")
        else:
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                collection = serializer.save()
                if 'destination_collection' in record:
                    collection.destination_collection.set(record['destination_collection'])
            else:
                errors.append(f"Validation error in new record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")
    
    if missing_destinations:
        raise ValueError(f"Destinations with the following titles do not exist: {', '.join(missing_destinations)}")

    if errors:
        raise ValueError("Errors occurred during processing:\n" + "\n".join(errors))



from datetime import datetime

def parse_date(date_str):
    """ Try different date formats and return a datetime object. """
    for fmt in ('%Y-%m-%d', '%m/%d/%y', '%m/%d/%Y'):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Date format for '{date_str}' is not supported.")

def create_update_departures(my_model, my_serializer, data, unique_field_name):
    errors = []
    missing_destinations = []

    for record in data:
        # Process destination_trip_names, splitting by comma
        if 'destination_trip_names' in record:
            destination_names_str = record['destination_trip_names']
            destination_names = [name.strip() for name in destination_names_str.split(',')]

            destination_ids = []
            for destination_name in destination_names:
                destination_obj = Destination.objects.filter(destination_title=destination_name).first()
                if not destination_obj:
                    missing_destinations.append(destination_name)
                else:
                    destination_ids.append(destination_obj.id)

            if not destination_ids:
                errors.append(f"No valid destinations found in 'destination_trip_names' for record with {unique_field_name}='{record[unique_field_name]}'.")
                continue

            record['destination_trip'] = destination_ids[0]  # Assuming one destination per record for simplicity.
        else:
            errors.append(f"destination_trip_names field is required in record with {unique_field_name}='{record[unique_field_name]}'.")
            continue

        # Handle date conversion with flexible format handling
        if 'upcoming_departure_date' in record:
            try:
                record['upcoming_departure_date'] = parse_date(record['upcoming_departure_date'])
            except ValueError as e:
                errors.append(f"Invalid date format in record with upcoming_departure_date='{record['upcoming_departure_date']}': {str(e)}")
                continue

        existing_data = my_model.objects.filter(destination_trip=record['destination_trip'], upcoming_departure_date=record['upcoming_departure_date'])
        
        if existing_data.exists():
            existing_data = existing_data.first()
            serializer = my_serializer(existing_data, data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                errors.append(f"Validation error in record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")
        else:
            serializer = my_serializer(data=record)
            if serializer.is_valid():
                serializer.save()
            else:
                errors.append(f"Validation error in new record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")

    if missing_destinations:
        raise ValueError(f"Destinations with the following titles do not exist: {', '.join(missing_destinations)}")

    if errors:
        raise ValueError("Errors occurred during processing:\n" + "\n".join(errors))


import json
import traceback
from datetime import datetime

import json
from datetime import datetime

def create_update_destinations(my_model, my_serializer, data, unique_field_name, request):
    errors = []
    missing_packages = []
    saved_records = 0

    for record in data:
        try:
            # Ignore all image fields if present
            image_fields = ['featured_image', 'trip_map_image', 'image']
            for image_field in image_fields:
                if image_field in record:
                    del record[image_field]

            # Resolve the ManyToMany field (packages)
            if 'packages_names' in record:
                package_names = record['packages_names']

                # Ensure package_names is treated as a list
                if isinstance(package_names, str):
                    package_names = [package_names]  # Convert to list if it's a single string
                
                package_ids = []
                for package_name in package_names:
                    package_obj = Package.objects.filter(name=package_name).first()
                    
                    if not package_obj:
                        missing_packages.append(package_name)
                    else:
                        package_ids.append(package_obj.id)

                if missing_packages:
                    errors.append(f"Packages with the following names do not exist and won't be created: {', '.join(missing_packages)}")
                    continue  # Skip this record and move to the next one

                record['packages'] = package_ids
            else:
                errors.append(f"The 'packages_names' field is required in record with {unique_field_name}='{record[unique_field_name]}'.")
                continue

            # Provide default departure data if none is provided
            if 'departures' not in record or not record['departures']:
                record['departures'] = json.dumps([{
                    "upcoming_departure_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "upcoming_departure_status": False,
                    "upcoming_departure_price": 0
                }])
            else:
                try:
                    # Convert departures to JSON string if it's provided
                    record['departures'] = json.dumps(record['departures']) if isinstance(record['departures'], list) else record['departures']
                except Exception as e:
                    errors.append(f"Error processing departures data for record with {unique_field_name}='{record[unique_field_name]}': {str(e)}")
                    record['departures'] = json.dumps([])  # Set to empty list if there's an error

            # Debugging: Print out the record before sending it to the serializer
            print(f"Debug: Processing record - {record}")

            # Handling other fields and creating or updating the Destination record
            existing_data = my_model.objects.filter(**{unique_field_name: record[unique_field_name]})
            
            if existing_data.exists():
                existing_data = existing_data.first()  # Get the existing record based on the unique field
                
                serializer = my_serializer(existing_data, data=record, context={'request': request})
                if serializer.is_valid():
                    try:
                        destination = serializer.save()
                        if 'packages' in record:
                            destination.packages.set(record['packages'])  # Update the ManyToMany field
                        saved_records += 1  # Count successful saves
                        print(f"Successfully updated record: {record[unique_field_name]}")
                    except Exception as e:
                        errors.append(f"Error saving record with {unique_field_name}='{record[unique_field_name]}': {str(e)}\nTraceback:\n{traceback.format_exc()}")
                else:
                    errors.append(f"Validation error in record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")
            else:
                # Create a new record
                serializer = my_serializer(data=record, context={'request': request})
                if serializer.is_valid():
                    try:
                        destination = serializer.save()
                        if 'packages' in record:
                            destination.packages.set(record['packages'])  # Set the ManyToMany field
                        saved_records += 1  # Count successful saves
                        print(f"Successfully created new record: {record[unique_field_name]}")
                    except Exception as e:
                        errors.append(f"Error saving new record with {unique_field_name}='{record[unique_field_name]}': {str(e)}\nTraceback:\n{traceback.format_exc()}")
                else:
                    errors.append(f"Validation error in new record with {unique_field_name}='{record[unique_field_name]}': {serializer.errors}")
        except Exception as e:
            errors.append(f"General error processing record with {unique_field_name}='{record.get(unique_field_name, 'unknown')}': {str(e)}\nTraceback:\n{traceback.format_exc()}")

    # Log errors but do not raise an exception
    if errors:
        print("Errors occurred during processing:\n" + "\n".join(errors))

    print(f"Total records saved successfully: {saved_records}")
