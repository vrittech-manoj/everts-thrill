from rest_framework import serializers
from ..models import Destination, DestinationGalleryImages, Departure, Package
from destination.serializers.package_serializers import PackageRetrieveSerializers
import ast

def str_to_list(data,value_to_convert):
    try:
        mutable_data = data.dict()
    except:
        mutable_data = data
    value_to_convert_data = mutable_data[value_to_convert]
    if isinstance(value_to_convert_data,list):# type(value_to_convert_data) == list:
        
        return mutable_data
    try:
        variations = ast.literal_eval(value_to_convert_data)
        mutable_data[value_to_convert] = variations
        return mutable_data
    except ValueError as e:
        raise serializers.ValidationError({f'{value_to_convert}': str(e)})
    

class PackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
    
class DestinationGalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationGalleryImages
        fields = '__all__'

class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'

class DestinationlistUserSerializers(serializers.ModelSerializer):
    # galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    # destination_departures = DepartureSerializer(many=True, read_only=True)
    # packages= PackageSerializers(many = True, read_only = True)

    class Meta:
        model = Destination
        fields = [
            'public_id',
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
        ]

class DestinationlistAdminSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = DepartureSerializer(many=True, read_only=True)
    packages= PackageSerializers(many = True, read_only = True)

    class Meta:
        model = Destination
        fields = [
            'public_id',
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
        ]

class DestinationRetrieveUserSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = DepartureSerializer(many=True, read_only=True)
    packages= PackageSerializers(many = True, read_only = True)

    class Meta:
        model = Destination
        fields = '__all__'

class DestinationRetrieveAdminSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True, read_only=True)
    destination_departures = DepartureSerializer(many=True, read_only=True)
    packages= PackageSerializers(many = True, read_only = True)

    class Meta:
        model = Destination
        fields = '__all__'
        
class DestinationWriteSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True,read_only = True)
    destination_departures = DepartureSerializer(many=True, read_only = True)
    packages= PackageSerializers(many = True, read_only = True)
    
    def to_internal_value(self, data):
        if data.get('packages'):
            data = str_to_list(data,'packages')
            return super().to_internal_value(data)
        return super().to_internal_value(data)

    class Meta:
        model = Destination
        fields = '__all__'
        # exclude = ['packages']

    def create(self, validated_data):
        packages_data = validated_data.pop('packages', [])

        departures_data = self.context.get('request').data.get('departures')
        import json
        departures_data =  json.loads(departures_data)
       

        images_data = []
        for key in self.context['request'].FILES:
            if key.startswith('images['):
                images_data.append(self.context['request'].FILES[key])

        destination = Destination.objects.create(**validated_data)
        departures_data = [ {'destination_trip':destination.id,**departure} for departure in departures_data]
        
        departure_serializers = DepartureSerializer(data=departures_data,many=True)
        if departure_serializers.is_valid(raise_exception=True):
            departure_serializers.save()
        else:
            print("This  is not valid ")
        
        if packages_data:
            destination.packages.set(packages_data)
        
      
     # Handle image uploads
        for image_file in images_data:
            DestinationGalleryImages.objects.create(destination_trip=destination, image=image_file)
        return destination
    
def update(self, instance, validated_data):
    # Parse departures data from request
    departures_data = self.context.get('request').data.get('departures')
    import json
    if departures_data:
        departures_data = json.loads(departures_data)

    # Parse images data from request
    images_data = []
    for key in self.context['request'].FILES:
        if key.startswith('images['):
            images_data.append(self.context['request'].FILES[key])

    # Call the parent's update method to update the instance
    instance = super().update(instance, validated_data)

    # Handling Departures
    if departures_data:
        # Get existing departure IDs from the database
        existing_departures = Departure.objects.filter(destination_trip=instance)
        existing_departure_ids = set(existing_departures.values_list('id', flat=True))

        # Extract the provided departure IDs from the request data
        provided_departure_ids = set([departure.get('id') for departure in departures_data if departure.get('id')])

        # Delete departures that are not in the provided data
        departures_to_delete = existing_departure_ids - provided_departure_ids
        Departure.objects.filter(id__in=departures_to_delete).delete()

        # Update or create departures
        for departure_data in departures_data:
            departure_id = departure_data.pop('id', None)
            if departure_id:
                # Update the existing departure
                departure_instance = Departure.objects.get(id=departure_id, destination_trip=instance)
                for key, value in departure_data.items():
                    setattr(departure_instance, key, value)
                departure_instance.save()
            else:
                # Create a new departure if the departure does not exist
                Departure.objects.create(destination_trip=instance, **departure_data)

    # Handling Images
    if images_data:
        # Collect all sent image ids if they are part of the update
        sent_image_ids = set()
        for image_data in images_data:
            # If updating existing images, ensure IDs are being captured
            sent_image_ids.add(image_data.name.split('[')[1].split(']')[0])

        # Delete images that are not in the sent images data
        DestinationGalleryImages.objects.filter(destination_trip=instance).exclude(id__in=sent_image_ids).delete()

        # Add or update images
        for image_data in images_data:
            # Check if the image already exists, if yes, update it
            existing_image_id = image_data.name.split('[')[1].split(']')[0]
            if existing_image_id:
                existing_image = DestinationGalleryImages.objects.get(id=existing_image_id, destination_trip=instance)
                existing_image.image = image_data
                existing_image.save()
            else:
                # Otherwise, create a new image entry
                DestinationGalleryImages.objects.create(destination_trip=instance, image=image_data)
    else:
        # If no image data is sent, delete all existing images related to this destination_trip
        DestinationGalleryImages.objects.filter(destination_trip=instance).delete()

    return instance
