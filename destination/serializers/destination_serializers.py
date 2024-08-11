from rest_framework import serializers
from ..models import Destination, DestinationGalleryImages, Departure

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

    class Meta:
        model = Destination
        fields = '__all__'

class DestinationlistAdminSerializers(serializers.ModelSerializer):
    images = DestinationGalleryImagesSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

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

    class Meta:
        model = Destination
        fields = '__all__'

    def create(self, validated_data):
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])
        holiday_trip = Destination.objects.create(**validated_data)


        for departure_data in departures_data:
            Departure.objects.create(holiday_trip=holiday_trip, **departure_data)

        for image_data in images_data:
            DestinationGalleryImages.objects.create(holiday_trip=holiday_trip, **image_data)

        return holiday_trip

    def update(self, instance, validated_data):
        faqs_data = validated_data.pop('faqs', [])
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        # Update other fields similarly
        instance.save()

            # Process departures using update_or_create
        for departure_data in departures_data:
            departure_id = departure_data.get('id')
            if departure_id:
                # Assuming 'id' is a unique identifier for Departure
                departure, created = Departure.objects.update_or_create(
                    id=departure_id,
                    defaults={key: val for key, val in departure_data.items() if key != 'id'}
                )
            else:
                # Create new departure if no ID is provided
                Departure.objects.create(destination=instance, **departure_data)
                

        for image_data in images_data:
            DestinationGalleryImages.objects.create(holiday_trip=instance, **image_data)

        return instance

class DestinationSerializer(serializers.ModelSerializer):
    images = DestinationGalleryImagesSerializer(many=True, required=False)
    departures = DepartureSerializer(many=True, required=False)

    class Meta:
        model = Destination
        fields = '__all__'

    def create(self, validated_data):
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])
        holiday_trip = Destination.objects.create(**validated_data)

        for departure_data in departures_data:
            Departure.objects.create(holiday_trip=holiday_trip, **departure_data)

        for image_data in images_data:
            DestinationGalleryImages.objects.create(holiday_trip=holiday_trip, **image_data)

        return holiday_trip

    def update(self, instance, validated_data):
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        # Update other fields similarly
        instance.save()

        # Update Departures
        instance.departures.all().delete()  # Clear existing departures
        for departure_data in departures_data:
            Departure.objects.create(holiday_trip=instance, **departure_data)

        # Update Images
        instance.images.all().delete()  # Clear existing images
        for image_data in images_data:
            DestinationGalleryImages.objects.create(holiday_trip=instance, **image_data)

        return instance
