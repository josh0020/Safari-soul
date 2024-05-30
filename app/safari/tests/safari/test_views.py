import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from safari.models import CulturalAttraction, Destination, TourPackage, Booking, Customer
from safari.serializers import CulturalAttractionSerializer, DestinationSerializer, TourPackageSerializer, BookingSerializer

@pytest.mark.django_db
def test_api_overview():
    client = APIClient()
    url = reverse('api_overview')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_cultural_attraction_viewset():
    client = APIClient()
    url = reverse('cultural_attraction_set-list')
    response = client.get(url)

    asset_1 = CulturalAttraction.objects.create(title='Attraction 1', description='Description 1')
    url2 = reverse('cultural_attraction_set-detail', args=[1])
    response2 = client.get(url2)
    assert response.status_code == status.HTTP_200_OK
    assert response2.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_destination_viewset():
    client = APIClient()
    url = reverse('destination_set-list')
    response = client.get(url)

    asset_1 = CulturalAttraction.objects.create(title='Attraction 1', description='Description 1')
    asset_2 = Destination.objects.create(title='Attraction 1', description='Description 1', cultural_attraction=asset_1)
    url2 = reverse('destination_set-detail', args=[1])
    response2 = client.get(url2)
    assert response.status_code == status.HTTP_200_OK
    assert response2.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_tour_package_viewset():
    client = APIClient()
    url = reverse('tourpackage_set-list')
    response = client.get(url)

    asset_1 = CulturalAttraction.objects.create(title='Attraction 1', description='Description 1')
    asset_2 = Destination.objects.create(title='Attraction 1', description='Description 1', cultural_attraction=asset_1)
    asset_3 = TourPackage.objects.create(title='Attraction 1', description='Description 1', price=5400, start_date='2023-11-30')
    url2 = reverse('destination_set-detail', args=[1])
    response2 = client.get(url2)
    assert response.status_code == status.HTTP_200_OK
    assert response2.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_customer_viewset():
    client = APIClient()
    url = reverse('customer_set-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_booking_viewset():
    client = APIClient()
    url = reverse('booking_set-list')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_cultural_attraction_list_view():
    client = APIClient()
    url = reverse('cultural_attractions')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_cultural_attraction_detail_view():
    cultural_attraction = CulturalAttraction.objects.create(title='Attraction 1', description='Description 1')
    client = APIClient()
    url = reverse('cultural_attraction', kwargs={'pk': cultural_attraction.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_destination_list_view():
    client = APIClient()
    url = reverse('destinations')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_destination_detail_view():
    cultural_attraction = CulturalAttraction.objects.create(title='Attraction 1', description='Description 1')
    destination = Destination.objects.create(title='Destination 1', description='Description 1', cultural_attraction=cultural_attraction)
    client = APIClient()
    url = reverse('destination', kwargs={'pk': destination.pk})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

