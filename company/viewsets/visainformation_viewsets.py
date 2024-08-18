from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import VisaInformation
from ..serializers.visainformation_serializers import VisaInformationListSerializers, VisaInformationRetrieveSerializers, VisaInformationWriteSerializers
from ..utilities.importbase import *

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class visainformationViewsets(viewsets.ModelViewSet):
    serializer_class = VisaInformationListSerializers
    permission_classes = [companyPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset = VisaInformation.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return VisaInformationWriteSerializers
        elif self.action == 'retrieve':
            return VisaInformationRetrieveSerializers
        return super().get_serializer_class()

    @action(detail=False, methods=['post'], name="create-update", url_path="url_path")
    def action_name(self, request, *args, **kwargs):
        description = request.data.get('description', None)
        
        if description is None:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        visa_information = VisaInformation.objects.all()
        
        if visa_information.exists():
            # Update the existing visa information
            visa_information = visa_information.first()
            visa_information.description = description
            visa_information.save()
            return Response({"message": "Visa information updated successfully."}, status=status.HTTP_200_OK)
        else:
            # Create new visa information
            new_visa_information = VisaInformation.objects.create(description=description)
            return Response({"message": "Visa information created successfully.", "id": new_visa_information.id}, status=status.HTTP_201_CREATED)
