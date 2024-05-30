from rest_framework import serializers
from .models import Customer, CulturalAttraction, Destination, TourPackage, Booking

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        return representation

class CulturalAttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalAttraction
        fields = '__all__'

class DestinationSerializer(serializers.ModelSerializer):
    cultural_attraction = CulturalAttractionSerializer(read_only=True)

    class Meta:
        model = Destination
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        cultural_attraction = instance.cultural_attraction

        if cultural_attraction:
            representation['cultural_attraction'] = cultural_attraction.title
        else:
            representation['cultural_attraction'] = None

        return representation

class TourPackageSerializer(serializers.ModelSerializer):
    destination = DestinationSerializer(read_only=True)

    class Meta:
        model = TourPackage
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['destination'] = instance.destination.title
        return representation

class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    tour_package = TourPackageSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['customer'] = instance.customer.user.username
        representation['tour_package'] = instance.tour_package.title
        return representation
