from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, CulturalAttraction, Destination, TourPackage, Booking
from .serializers import CulturalAttractionSerializer, CustomerSerializer, DestinationSerializer, TourPackageSerializer, BookingSerializer


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Culturural_attractions' : '/api/v1/cultural_attractions',
        'Culturural_attractions/<int:pk>' : '/api/v1/cultural_attractions/<pk>',
        'destinations' : '/api/v1/destinations',
        'destinations/<int:pk>' : '/api/v1/destinations/<pk>'
    }
    return Response(api_urls)


class CulturalAttractionViewSet(viewsets.ModelViewSet):
    queryset = CulturalAttraction.objects.all()
    serializer_class = CulturalAttractionSerializer
    lookup_field = 'slug'

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = 'slug'

class TourPackageViewSet(viewsets.ModelViewSet):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    lookup_field = 'slug'
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'slug'

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'slug'


# external apis for cultural attraction and destination
class CulturalAttractionListView(generics.ListAPIView):
    queryset = CulturalAttraction.objects.all()
    serializer_class = CulturalAttractionSerializer

class CulturalAttractionDetailView(generics.RetrieveAPIView):
    queryset = CulturalAttraction.objects.all()
    serializer_class = CulturalAttractionSerializer

class DestinationListView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetailView(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
