from rest_framework import serializers
from ..models import Destination, HolidayTripGalleryImages, Faqs, Departure

class HolidayTripGalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayTripGalleryImages
        fields = '__all__'

class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = ['id', 'title', 'description']

class DepartureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departure
        fields = ['id', 'upcoming_departure_date', 'upcoming_departure_status', 'upcoming_departure_price']

class HolidayTriplistUserSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)
    faqs = FaqsSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

class HolidayTriplistAdminSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)
    faqs = FaqsSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

class HolidayTripRetrieveUserSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)
    faqs = FaqsSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

class HolidayTripRetrieveAdminSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, read_only=True)
    faqs = FaqsSerializer(many=True, read_only=True)
    departures = DepartureSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

class HolidayTripWriteSerializers(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, required=False)
    faqs = FaqsSerializer(many=True, required=False)
    departures = DepartureSerializer(many=True, required=False)

    class Meta:
        model = Destination
        fields = '__all__'

    def create(self, validated_data):
        faqs_data = validated_data.pop('faqs', [])
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])
        holiday_trip = Destination.objects.create(**validated_data)

        for faq_data in faqs_data:
            Faqs.objects.create(holiday_trip=holiday_trip, **faq_data)

        for departure_data in departures_data:
            Departure.objects.create(holiday_trip=holiday_trip, **departure_data)

        for image_data in images_data:
            HolidayTripGalleryImages.objects.create(holiday_trip=holiday_trip, **image_data)

        return holiday_trip

    def update(self, instance, validated_data):
        faqs_data = validated_data.pop('faqs', [])
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        # Update other fields similarly
        instance.save()

        # Update FAQs
        instance.faqs.all().delete()  # Clear existing FAQs
        for faq_data in faqs_data:
            Faqs.objects.create(holiday_trip=instance, **faq_data)

        # Update Departures
        instance.departures.all().delete()  # Clear existing departures
        for departure_data in departures_data:
            Departure.objects.create(holiday_trip=instance, **departure_data)

        # Update Images
        instance.images.all().delete()  # Clear existing images
        for image_data in images_data:
            HolidayTripGalleryImages.objects.create(holiday_trip=instance, **image_data)

        return instance

class HolidayTripSerializer(serializers.ModelSerializer):
    images = HolidayTripGalleryImagesSerializer(many=True, required=False)
    faqs = FaqsSerializer(many=True, required=False)
    departures = DepartureSerializer(many=True, required=False)

    class Meta:
        model = Destination
        fields = '__all__'

    def create(self, validated_data):
        faqs_data = validated_data.pop('faqs', [])
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])
        holiday_trip = Destination.objects.create(**validated_data)

        for faq_data in faqs_data:
            Faqs.objects.create(holiday_trip=holiday_trip, **faq_data)

        for departure_data in departures_data:
            Departure.objects.create(holiday_trip=holiday_trip, **departure_data)

        for image_data in images_data:
            HolidayTripGalleryImages.objects.create(holiday_trip=holiday_trip, **image_data)

        return holiday_trip

    def update(self, instance, validated_data):
        faqs_data = validated_data.pop('faqs', [])
        departures_data = validated_data.pop('departures', [])
        images_data = validated_data.pop('images', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        # Update other fields similarly
        instance.save()

        # Update FAQs
        instance.faqs.all().delete()  # Clear existing FAQs
        for faq_data in faqs_data:
            Faqs.objects.create(holiday_trip=instance, **faq_data)

        # Update Departures
        instance.departures.all().delete()  # Clear existing departures
        for departure_data in departures_data:
            Departure.objects.create(holiday_trip=instance, **departure_data)

        # Update Images
        instance.images.all().delete()  # Clear existing images
        for image_data in images_data:
            HolidayTripGalleryImages.objects.create(holiday_trip=instance, **image_data)

        return instance
