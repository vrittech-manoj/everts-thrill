from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import AboutUs
from ..serializers.aboutus_serializers import AboutUsListSerializers, AboutUsRetrieveSerializers, AboutUsWriteSerializers
from ..utilities.importbase import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class aboutusViewsets(viewsets.ModelViewSet):
    serializer_class = AboutUsListSerializers
    # permission_classes = [companyPermission]
    # authentication_classes = [JWTAuthentication]
    #pagination_class = MyPageNumberPagination
    queryset = AboutUs.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    ordering_fields = ['id']

    # filterset_fields = {
    #     'id': ['exact'],
    # }

    def get_queryset(self):
        queryset = super().get_queryset()
        #return queryset.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AboutUsWriteSerializers
        elif self.action == 'retrieve':
            return AboutUsRetrieveSerializers
        return super().get_serializer_class()

    # @action(detail=False, methods=['get'], name="action_name", url_path="url_path")
    # def action_name(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'], name="create-update", url_path="create-about-us")
    def create_update_about_us(self, request, *args, **kwargs):
        description = request.data.get('description', None)

        if not description:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)

        about_us = AboutUs.objects.all()

        if about_us.exists():
            # Update the existing AboutUs entry
            about_us = about_us.first()
            about_us.description = description
            about_us.save()
            return Response({"message": "About Us section updated successfully."}, status=status.HTTP_200_OK)
        else:
            # Create a new AboutUs entry
            new_about_us = AboutUs.objects.create(description=description)
            return Response({"message": "About Us section created successfully.", "about_us_id": new_about_us.id}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get', 'put'], name="retrieve-update", url_path="detail-about-us")
    def retrieve_update_about_us(self, request, *args, **kwargs):
        try:
            # Assuming there's only one AboutUs entry, get the first one.
            about_us = AboutUs.objects.first()

            if not about_us:
                return Response({"data": None}, status=status.HTTP_200_OK)

        except AboutUs.DoesNotExist:
            return Response({"error": "About Us section not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            # Retrieve the About Us entry
            serializer = AboutUsRetrieveSerializers(about_us)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            description = request.data.get('description', None)

            if not description:
                return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)

            about_us.description = description
            about_us.save()
            return Response({"message": "About Us section updated successfully."}, status=status.HTTP_200_OK)


