from rest_framework import serializers
from ..models import DestinationBook
from accounts.models import CustomUser
from airlines.models import Airlines
from activities.models import Activity
from destination.models import Package,Destination
        
class BookingAirlinesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = '__all__'
        
class BookingActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['name']
        
class BookingPackageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['name']
        
class BookingDestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = ['id','destination_title','duration','group_size','best_season','meals']
# ('public_id', 'slug', 'destination_title', 'packages', 'price', 'price_type', 'is_price', 'featured_image', 'overview', 'inclusion_and_exclusion', 'ltinerary', 'trip_map_url', 'trip_map_image', 'gear_and_equipment', 'useful_information', 'duration', 'trip_grade', 'best_season', 'max_altitude', 'meals', 'nature_of_trip', 'accommodation', 'group_size', )
class DestinationBookListSerializers(serializers.ModelSerializer):
    activity = BookingActivitySerializers(read_only = True)
    package = BookingPackageSerializers(read_only = True)
    destination = BookingDestinationSerializers(read_only = True)
    class Meta:
        model = DestinationBook
        fields = '__all__'
        
class DestinationBookRetrieveSerializers(serializers.ModelSerializer):
    activity = BookingActivitySerializers(read_only = True)
    package = BookingPackageSerializers(read_only = True)
    destination = BookingDestinationSerializers(read_only = True)
    class Meta:
        model = DestinationBook
        fields = '__all__'

class DestinationBookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = DestinationBook
        fields = '__all__'
        