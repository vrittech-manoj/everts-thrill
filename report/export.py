from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
import csv
from django.apps import apps
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class GetSampleAPIView(APIView):
    """
    API view to generate and download sample data in CSV format for different models.
    """
    
    model_mapping = {
        "package": "destination.Package",
        "destination": "destination.Destination",
        "gallery-images": "destination.DestinationGalleryImages",
        "review": "review.Review",
        "collection": "collection.Collection",
        "departure": "departure.Departure",
        "destination-book": "booking.DestinationBook",
        "activity": "activities.Activity",
    }

    excluded_fields = ['id', 'slug', 'public_id', 'created_date', 'updated_date']

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
        model_class_path = self.model_mapping.get(type)

        if not model_class_path:
            return Response({"message": 'Unknown type'}, status=status.HTTP_400_BAD_REQUEST)

        # Dynamically import the model class
        app_label, model_name = model_class_path.split(".")
        model_class = apps.get_model(app_label=app_label, model_name=model_name)

        # Get all fields of the model, excluding specified fields
        column_list = []
        for field in model_class._meta.get_fields():
            if field.name not in self.excluded_fields:
                if field.is_relation:
                    if field.many_to_one or field.one_to_one:
                        # For ForeignKey or OneToOneField, include the related model's primary key or string representation
                        column_list.append(f"{field.name}_names")
                    elif field.many_to_many:
                        # For ManyToManyField, append related objects' names
                        column_list.append(f"{field.name}_names")
                else:
                    column_list.append(field.name)

        queryset = model_class.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{type}.csv"'

        writer = csv.writer(response)

        # Write the header row
        writer.writerow(column_list)

        # Write data rows
        for data in queryset:
            data_row = []
            for column in column_list:
                if column.endswith("_id"):
                    # ForeignKey or OneToOneField relation, get related object's ID
                    related_field_name = column.replace("_id", "")
                    related_object = getattr(data, related_field_name)
                    data_row.append(getattr(related_object, 'id', None) if related_object else None)
                elif column.endswith("_names"):
                    # ManyToManyField relation, get related objects' names
                    related_field_name = column.replace("_names", "")
                    related_objects = getattr(data, related_field_name).all()
                    related_names = ", ".join(str(obj) for obj in related_objects)
                    data_row.append(related_names)
                else:
                    data_row.append(getattr(data, column))
            writer.writerow(data_row)

        return response
