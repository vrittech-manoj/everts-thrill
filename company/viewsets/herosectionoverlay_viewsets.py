from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from ..models import HeroSectionOverlay
from ..serializers.herosectionoverlay_serializers import HeroSectionOverlayListSerializers, HeroSectionOverlayRetrieveSerializers, HeroSectionOverlayWriteSerializers
from ..utilities.importbase import *

class herosectionoverlayViewsets(viewsets.ModelViewSet):
    serializer_class = HeroSectionOverlayListSerializers
    permission_classes = [companyPermission]
    pagination_class = MyPageNumberPagination
    queryset = HeroSectionOverlay.objects.all()

    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id','overlay_text']
    ordering_fields = ['id','overlay_text']

    filterset_fields = {
        'id': ['exact'],
        'overlay_text': ['exact'],
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return HeroSectionOverlayWriteSerializers
        elif self.action == 'retrieve':
            return HeroSectionOverlayRetrieveSerializers
        return super().get_serializer_class()
    
    
    @action(detail=False, methods=['post'], name="create-update", url_path="create-hero-section-overlay")
    def create_update_hero_section_overlay(self, request, *args, **kwargs):
        overlay_text = request.data.get('overlay_text', None)
        button_text = request.data.get('button_text', None)
        button_link = request.data.get('button_link', None)
        
        # Directly use the boolean values from the frontend without converting them
        is_button = request.data.get('is_button', False)
        is_overlay_text = request.data.get('is_overlay_text', False)

        if overlay_text is None and is_overlay_text:
            return Response({"error": "Overlay text is required when is_overlay_text is True."}, status=status.HTTP_400_BAD_REQUEST)

        hero_section_overlay = HeroSectionOverlay.objects.all()

        if hero_section_overlay.exists():
            # Update the existing hero section overlay
            hero_section_overlay = hero_section_overlay.first()
            hero_section_overlay.overlay_text = overlay_text
            hero_section_overlay.button_text = button_text
            hero_section_overlay.button_link = button_link
            hero_section_overlay.is_button = is_button
            hero_section_overlay.is_overlay_text = is_overlay_text
            hero_section_overlay.save()
            return Response({"message": "Hero section overlay updated successfully."}, status=status.HTTP_200_OK)
        else:
            # Create a new hero section overlay
            new_overlay = HeroSectionOverlay.objects.create(
                overlay_text=overlay_text,
                button_text=button_text,
                button_link=button_link,
                is_button=is_button,
                is_overlay_text=is_overlay_text
            )
            return Response({"message": "Hero section overlay created successfully.", "overlay_id": new_overlay.id}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get', 'put'], name="retrieve-update", url_path="detail-hero-section-overlay")
    def retrieve_update_hero_section_overlay(self, request, *args, **kwargs):
        try:
            # Assuming there's only one hero section overlay, get the first one.
            hero_section_overlay = HeroSectionOverlay.objects.first()

            if not hero_section_overlay:
                return Response({"data": None}, status=status.HTTP_200_OK)

        except HeroSectionOverlay.DoesNotExist:
            return Response({"error": "Hero section overlay not found."}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            # Retrieve the hero section overlay
            serializer = HeroSectionOverlayRetrieveSerializers(hero_section_overlay)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            # Update the hero section overlay
            overlay_text = request.data.get('overlay_text', None)
            button_text = request.data.get('button_text', None)
            button_link = request.data.get('button_link', None)
            
            # Directly use the boolean values from the frontend without converting them
            is_button = request.data.get('is_button', False)
            is_overlay_text = request.data.get('is_overlay_text', False)

            if overlay_text is None and is_overlay_text:
                return Response({"error": "Overlay text is required when is_overlay_text is True."}, status=status.HTTP_400_BAD_REQUEST)

            hero_section_overlay.overlay_text = overlay_text
            hero_section_overlay.button_text = button_text
            hero_section_overlay.button_link = button_link
            hero_section_overlay.is_button = is_button
            hero_section_overlay.is_overlay_text = is_overlay_text
            hero_section_overlay.save()
            return Response({"message": "Hero section overlay updated successfully."}, status=status.HTTP_200_OK)
