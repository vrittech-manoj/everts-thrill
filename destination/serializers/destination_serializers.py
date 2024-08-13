from rest_framework import serializers
from ..models import Destination, DestinationGalleryImages, Departure
from destination.serializers.package_serializers import PackageRetrieveSerializers
import ast

def str_to_list(data,value_to_convert):
    print("1")
    try:
        mutable_data = data.dict()
    except:
        mutable_data = data
    print(value_to_convert)
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
        fields = ['id', 'upcoming_departure_date', 'upcoming_departure_status', 'upcoming_departure_price']

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
    images = DestinationGalleryImagesSerializer(many=True, required=False)
    departures = DepartureSerializer(many=True, required=False)
    
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
        # departures_data = validated_data.pop('departures', [])
        # Manually parse departures data
        departures_data = []
        for key, value in self.context['request'].data.items():
            if key.startswith('departures'):
                index = int(key.split('[')[1].split(']')[0])
                field_name = key.split('[')[2].split(']')[0]
                while len(departures_data) <= index:
                    departures_data.append({})
                if field_name == 'upcoming_departure_status':
                    value = value.lower() == 'true'  # Convert "true"/"false" strings to boolean
                departures_data[index][field_name] = value
        # images_data = self.context['request'].FILES.getlist('images', [])
         # Collect all image files with keys like 'images[0]', 'images[1]', etc.
        images_data = []
        for key in self.context['request'].FILES:
            if key.startswith('images['):
                images_data.append(self.context['request'].FILES[key])

        destination = Destination.objects.create(**validated_data)
        
        if packages_data:
            destination.packages.set(packages_data)
        
        # Process departures data inside the loop
        for departure_data in departures_data:
            if departure_data:  # Ensure departure_data is not empty
                print("Departure", departure_data)  # Debugging statement
                Departure.objects.create(destination_trip=destination, **departure_data)                                                        
                
        print("Parsed Departures Data:", departures_data)

        # for departure_data in departures_data:
        #     Departure.objects.create(destination_trip=destination, **departure_data)

     # Handle image uploads
        for image_file in images_data:
            DestinationGalleryImages.objects.create(destination_trip=destination, image=image_file)
        return destination

    def update(self, instance, validated_data):
       
        # departures_data = validated_data.pop('departures', [])
        # Manually parse departures data
        departures_data = []
        for key, value in self.context['request'].data.items():
            if key.startswith('departures'):
                index = int(key.split('[')[1].split(']')[0])
                field_name = key.split('[')[2].split(']')[0]
                while len(departures_data) <= index:
                    departures_data.append({})
                if field_name == 'upcoming_departure_status':
                    value = value.lower() == 'true'  # Convert "true"/"false" strings to boolean
                departures_data[index][field_name] = value

        # images_data = self.context['request'].FILES.getlist('images', [])
        images_data = []
        for key in self.context['request'].FILES:
            if key.startswith('images['):
                images_data.append(self.context['request'].FILES[key])
        
        instance = super().update(instance, validated_data) 
        # instance.save()

        # Process departures data inside the loop
        for departure_data in departures_data:
            if departure_data:  # Ensure departure_data is not empty
                print("Departure", departure_data)  # Debugging statement
                Departure.objects.create(destination_trip=instance, **departure_data)
                    

        for image_data in images_data:
            # DestinationGalleryImages.objects.create(destination_trip=instance, **image_data)
            DestinationGalleryImages.objects.create(destination_trip=instance, image=image_data)

        return instance

