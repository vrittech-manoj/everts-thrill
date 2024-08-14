def update(self, instance, validated_data):
    departures_data = self.context.get('request').data.get('departures')
    import json
    departures_data = json.loads(departures_data)

    images_data = []
    for key in self.context['request'].FILES:
        if key.startswith('images['):
            images_data.append(self.context['request'].FILES[key])

    instance = super().update(instance, validated_data)

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
            # Creating a new departure if the departure does not exist
            Departure.objects.create(destination_trip=instance, **departure_data)

    # Handle images
    for image_data in images_data:
        DestinationGalleryImages.objects.create(destination_trip=instance, image=image_data)

    return instance
