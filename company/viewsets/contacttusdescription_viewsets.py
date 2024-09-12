from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import ContacttUsDescription
from ..serializers.contacttusdescription_serializers import (
    ContacttUsDescriptionListSerializers, 
    ContacttUsDescriptionRetrieveSerializers, 
    ContacttUsDescriptionWriteSerializers
)
from ..utilities.importbase import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class contacttusdescriptionViewsets(viewsets.ModelViewSet):
    serializer_class = ContacttUsDescriptionListSerializers
    permission_classes = [companyPermission]
    pagination_class = MyPageNumberPagination
    queryset = ContacttUsDescription.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']
    filterset_fields = {
        'id': ['exact'],
    }

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ContacttUsDescriptionWriteSerializers
        elif self.action == 'retrieve':
            return ContacttUsDescriptionRetrieveSerializers
        return super().get_serializer_class()

    @action(detail=False, methods=['post'], name="create-contact-us", url_path="create-contact-us")
    def create_update_contact_us(self, request, *args, **kwargs):
        description = request.data.get('description', None)

        if not description:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)

        contact_us = ContacttUsDescription.objects.all()

        if contact_us.exists():
            # Update the existing Contact Us entry
            contact_us_instance = contact_us.first()
            contact_us_instance.description = description
            contact_us_instance.save()
            return Response({"message": "Contact Us section updated successfully."}, status=status.HTTP_200_OK)
        else:
            # Create a new Contact Us entry
            new_contact_us = ContacttUsDescription.objects.create(description=description)
            return Response({"message": "Contact Us section created successfully.", "contact_us_id": new_contact_us.id}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get', 'put'], name="retrieve-update-contact-us", url_path="detail-contact-us")
    def retrieve_update_contact_us(self, request, *args, **kwargs):
        try:
            contact_us = ContacttUsDescription.objects.first()

            if not contact_us:
                return Response({"data": None}, status=status.HTTP_200_OK)

        except ContacttUsDescription.DoesNotExist:
            return Response({"error": "Contact Us section not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            # Retrieve the Contact Us entry
            serializer = ContacttUsDescriptionRetrieveSerializers(contact_us)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            description = request.data.get('description', None)

            if not description:
                return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)

            contact_us.description = description
            contact_us.save()
            return Response({"message": "Contact Us section updated successfully."}, status=status.HTTP_200_OK)
