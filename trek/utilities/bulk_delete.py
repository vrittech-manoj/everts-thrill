from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from blog.models import Blog
from holiday.models import  HolidayTrip,HolidayType
from queries.models import Queries 
from booking.models import HolidayTripBook

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
class BulkDelete(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'delete_ids': openapi.Schema(type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
                description='List of IDs to be deleted'),
        },
        required=['delete_ids', 'type'],
    ),
        # responses={200: MyResponseSerializer},
        operation_summary="Bulk Delete file",
        operation_description="Bulk Delete file",
    )
    
    def post(self, request,delete_type, *args, **kwargs):
        delete_ids = request.data.get('delete_ids')
        # type = request.data.get('type')
        
        if not delete_ids:
            return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        if delete_type == "blog":
            query = Blog.objects.filter(id__in=delete_ids)
        elif delete_type == "holiday-trip":
            query = HolidayTrip.objects.filter(id__in=delete_ids)
        elif delete_type == "holiday-trip-type":
            query = HolidayType.objects.filter(id__in=delete_ids)
        elif delete_type == "queries":
            query = Queries.objects.filter(id__in=delete_ids)
        elif delete_type == "booking":
            query = HolidayTripBook.objects.filter(id__in=delete_ids)
        # elif delete_type == "education-level":
        #     query = EducationLevel.objects.filter(id__in=delete_ids)
        # elif delete_type == "experience-level":
        #     query = WorkExperience.objects.filter(id__in=delete_ids)
        # elif delete_type == "job-timing":
        #     query = JobTiming.objects.filter(id__in=delete_ids)
        # elif delete_type == "work-location":
        #     query = JobLocation.objects.filter(id__in=delete_ids)
        else:
            return Response({"error": 'Unknown data type'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Perform the deletion
        query.delete()

        return Response({"message": "Data successfully deleted in bulk"}, status=status.HTTP_200_OK)

