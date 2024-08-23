from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
from django.http import HttpResponse
import csv
from jobutils.models import JobTiming,JobLocation,JobLevel
from job.models import JobCategory,Skills
from professions.models import  Profession
from company.models import CompanyType
from management.models import Branding

class getSample(APIView):
    def get(self, request, type, format=None):
            
            if type == "job-timing":
                queryset = JobTiming.objects.all()
                column_list = ['id','name','created_date']
            elif type == "job-level":
                queryset = JobLevel.objects.all()
                column_list = ['id','name','created_date']
            elif type == "job-location":
                queryset = JobLocation.objects.all()
                column_list = ['id','name','created_date']

            elif type == "job-category":
                queryset = JobCategory.objects.all()
                column_list = ['id','name','is_popular','slug','created_date']
    
            elif type == "profession":
                queryset = Profession.objects.all()
                column_list = ['id','name','slug','created_date']
            elif type == "skills":
                queryset = Skills.objects.all()
                column_list = ['id','name','category','created_date']
            elif type == "company-type":
                queryset = CompanyType.objects.all()
                column_list = ['id','type','slug','created_date']
            else:
                return Response({"message": 'Unknown type'}, status=status.HTTP_400_BAD_REQUEST)
            
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{type}.csv"'

            writer = csv.writer(response)

            # Write the header row
            writer.writerow(column_list)

            # Write data rows
            for data in queryset:
                data_lists = []
                for column in column_list:
                    data_lists.append(getattr(data,column))
                writer.writerow(data_lists)

            return response
    
class getBranding(APIView):
    def get(self, request, type, format=None):
        obj  = Branding.objects.all()
        if obj.exists():
            is_branding = obj.last().is_true
        else:
            is_branding = False
        return Response({"message": is_branding}, status=status.HTTP_200_OK)