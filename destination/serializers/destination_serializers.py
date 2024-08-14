from rest_framework import serializers
from ..models import Destination, DestinationGalleryImages, Departure
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
        print(type(variations))
        return mutable_data
    except ValueError as e:
        raise serializers.ValidationError({f'{value_to_convert}': str(e)})
    
class DestinationGalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationGalleryImages
        fields = '__all__'

class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = '__all__'

class DestinationlistUserSerializers(serializers.ModelSerializer):
    images = DestinationGalleryImagesSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)
    packages = PackageRetrieveSerializers(many=True)

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
            'images',  # Including the images
            'departures'
        ]

class DestinationlistAdminSerializers(serializers.ModelSerializer):
    images = DestinationGalleryImagesSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)
    packages = PackageRetrieveSerializers(many=True)

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
            'images',  # Including the images
            'departures'
        ]

class DestinationRetrieveUserSerializers(serializers.ModelSerializer):
    images = DestinationGalleryImagesSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

class DestinationRetrieveAdminSerializers(serializers.ModelSerializer):
    images = DestinationGalleryImagesSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

class DestinationWriteSerializers(serializers.ModelSerializer):
    galleryimages = DestinationGalleryImagesSerializer(many=True,read_only = True)
    destination_departures = DepartureSerializer(many=True, read_only = True)
    
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

        print("creating destinction")
        destination = Destination.objects.create(**validated_data)
        departures_data = [ {'destination_trip':destination.id,**departure} for departure in departures_data]
        print(departures_data)
        departure_serializers = DepartureSerializer(data=departures_data,many=True)
        if departure_serializers.is_valid(raise_exception=True):
            print(departure_serializers.data)
            departure_serializers.save()
        else:
            print("this  is not valid ")
        
        if packages_data:
            destination.packages.set(packages_data)
        
      
     # Handle image uploads
        for image_file in images_data:
            DestinationGalleryImages.objects.create(destination_trip=destination, image=image_file)
        return destination

    def update(self, instance, validated_data):
       
        # departures_data = validated_data.pop('departures', [])

        images_data = []
        for key in self.context['request'].FILES:
            if key.startswith('images['):
                images_data.append(self.context['request'].FILES[key])
        
        instance = super().update(instance, validated_data) 

        for image_data in images_data:
            DestinationGalleryImages.objects.create(destination_trip=instance, image=image_data)

        return instance

