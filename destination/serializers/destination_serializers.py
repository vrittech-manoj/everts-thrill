from rest_framework import serializers
from ..models import Destination, DestinationGalleryImages, Departure, Package
from destination.serializers.package_serializers import PackageRetrieveSerializers
import ast
from django.db import transaction
from rest_framework.exceptions import ValidationError
from django.db.models import Q
import json

MONTHS_MAPPING = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4,
    'may': 5, 'june': 6, 'july': 7, 'august': 8,
    'september': 9, 'october': 10, 'november': 11, 'december': 12
}


def str_to_list(data,value_to_convert):
    try:
        mutable_data = data.dict()
    except Exception:
        mutable_data = data
    value_to_convert_data = mutable_data[value_to_convert]
    if isinstance(value_to_convert_data,list):# type(value_to_convert_data) == list:

        return mutable_data
    try:
        variations = ast.literal_eval(value_to_convert_data)
        mutable_data[value_to_convert] = variations
        return mutable_data
    except ValueError as e:
        raise serializers.ValidationError({f'{value_to_convert}': str(e)}) from e
    

class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = [
            'id',
            'name',
            'image',]
    
class DestinationGalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationGalleryImages
        fields = '__all__'

class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'


class DestinationlistUserSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = DepartureSerializer(many=True, read_only=True)
    packages= PackageSerializers(many = True, read_only = True)

    class Meta:
        model = Destination
        fields = [
            'id',
            'slug',
            'destination_title',
            'packages',  # Including the package names
            'price',
            'price_type',
            'is_price',
            'featured_image',
            'overview',
            'inclusion_and_exclusion',
            'ltinerary',
            'trip_map_url',
            'trip_map_image',
            'gear_and_equipment',
            'useful_information',
            'duration',
            'trip_grade',
            'best_season',
            'max_altitude',
            'meals',
            'nature_of_trip',
            'accommodation',
            'group_size',
            'galleryimages',
            'destination_departures',
            
        ]

class DestinationlistAdminSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = DepartureSerializer(many=True, read_only=True)
    packages= PackageSerializers(many = True, read_only = True)

    class Meta:
        model = Destination
        fields = [
            'id',
            'slug',
            'destination_title',
            'packages',  # Including the package names
            'price',
            'price_type',
            'is_price',
            'featured_image',
            'overview',
            'inclusion_and_exclusion',
            'ltinerary',
            'trip_map_url',
            'trip_map_image',
            'gear_and_equipment',
            'useful_information',
            'duration',
            'trip_grade',
            'best_season',
            'max_altitude',
            'meals',
            'nature_of_trip',
            'accommodation',
            'group_size',
            'galleryimages',
            'destination_departures',
        ]

class DestinationRetrieveUserSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = serializers.SerializerMethodField()  
    packages= PackageSerializers(many = True, read_only = True)

    class Meta:
        model = Destination
        fields = '__all__'
    
    def get_destination_departures(self, obj):
        request = self.context.get('request')
        departure_month_name = request.query_params.get('departure_month')
        
        if departure_month_name:
            try:
                # Convert the full month name to the corresponding month number using MONTHS_MAPPING
                departure_month_number = MONTHS_MAPPING.get(departure_month_name.lower())
                
                if not departure_month_number:
                    raise ValidationError(f"Invalid month name '{departure_month_name}'. Please provide a valid full month name.")
                
                # Filter the departures by the month number
                upcoming_departures = obj.destination_departures.filter(
                    Q(upcoming_departure_date__month=departure_month_number)
                )
            except ValueError:
                upcoming_departures = obj.destination_departures.none()  # Invalid month name
        else:
            # If no month name is specified, return all departures
            upcoming_departures = obj.destination_departures.all()
        
        return DepartureSerializer(upcoming_departures, many=True).data

class DestinationRetrieveAdminSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = serializers.SerializerMethodField()  
    packages = PackageSerializers(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

    def get_destination_departures(self, obj):
        request = self.context.get('request')
        departure_month_name = request.query_params.get('departure_month')
        
        if departure_month_name:
            try:
                # Convert the full month name to the corresponding month number using MONTHS_MAPPING
                departure_month_number = MONTHS_MAPPING.get(departure_month_name.lower())
                
                if not departure_month_number:
                    raise ValidationError(f"Invalid month name '{departure_month_name}'. Please provide a valid full month name.")
                
                # Filter the departures by the month number
                upcoming_departures = obj.destination_departures.filter(
                    Q(upcoming_departure_date__month=departure_month_number)
                )
            except ValueError:
                upcoming_departures = obj.destination_departures.none()  # Invalid month name
        else:
            # If no month name is specified, return all departures
            upcoming_departures = obj.destination_departures.all()
        
        return DepartureSerializer(upcoming_departures, many=True).data
        
class DestinationWriteSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = DepartureSerializer(many=True, read_only=True)
    
    def to_internal_value(self, data):
        if data.get('packages'):
            data = str_to_list(data,'packages')
            return super().to_internal_value(data)
        return super().to_internal_value(data)


    class Meta:
        model = Destination
        fields = '__all__'
        # exclude = ['packages']
    @transaction.atomic
    def create(self, validated_data):
        packages_data = validated_data.pop('packages', [])

       # Load departures data from request and parse JSON
        departures_data = self.context.get('request').data.get('departures')
        import json
        departures_data = json.loads(departures_data)
       

        images_data = []
        for key in self.context['request'].FILES:
            if key.startswith('images['):
                images_data.append(self.context['request'].FILES[key])

        destination = Destination.objects.create(**validated_data)
        # Map destination ID to departures data
        departures_data = [{'destination_trip': destination.id, **departure} for departure in departures_data]

        # Validate and save departures data
        departure_serializers = DepartureSerializer(data=departures_data, many=True)
        if departure_serializers.is_valid(raise_exception=True):
            departure_serializers.save()
        else:
            print("Departures data is not valid")

        
        if packages_data:
            destination.packages.set(packages_data)
        
      
     # Handle image uploads
        for image_file in images_data:
            DestinationGalleryImages.objects.create(destination_trip=destination, image=image_file)
        return destination
    @transaction.atomic    
    def update(self, instance, validated_data):
        
        # Parse departures and images data from the request
        request = self.context.get('request')
        departures_data = json.loads(request.data.get('departures', '[]')) if request.data.get('departures') else None
        images_data = [file for key, file in request.FILES.items() if key.startswith('images[')]

        # Update the instance
        instance = super().update(instance, validated_data)

        # Handle Departures
        if departures_data:
            existing_departures = Departure.objects.filter(destination_trip=instance)
            existing_ids = set(existing_departures.values_list('id', flat=True))
            provided_ids = set([d.get('id') for d in departures_data if d.get('id')])

            # Delete departures not included in the new data
            Departure.objects.filter(id__in=(existing_ids - provided_ids)).delete()

            # Update or create departures
            for data in departures_data:
                departure_id = data.pop('id', None)
                data['upcoming_departure_status'] = True if data.get('upcoming_departure_status', False) == 'true' else False
                
                if departure_id and Departure.objects.filter(id=departure_id, destination_trip=instance).exists():
                    Departure.objects.filter(id=departure_id).update(**data)
                else:
                    Departure.objects.create(destination_trip=instance, **data)
        else:
            # Delete all if no data is provided
            Departure.objects.filter(destination_trip=instance).delete()

        # Handle Images
        if images_data:
            DestinationGalleryImages.objects.filter(destination_trip=instance).delete()  # Clear existing images
            for image_file in images_data:
                DestinationGalleryImages.objects.create(destination_trip=instance, image=image_file)

        return instance

