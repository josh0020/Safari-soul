import pytest
# from django.contrib.auth.models import User
from accounts.models import User
from safari.models import Customer, CulturalAttraction, Destination, TourPackage, Booking


@pytest.mark.django_db
def test_customer_model():
    user = User.objects.create(username='testuser', phonenumber='1234567890')
    customer = Customer.objects.create(user=user)
    assert customer.user == user
    assert customer.user.phonenumber == '1234567890'
    assert str(customer) == f'{user}'

@pytest.mark.django_db
def test_cultural_attraction_model():
    cultural_attraction = CulturalAttraction.objects.create(title='Attraction', description='Test description')
    assert cultural_attraction.title == 'Attraction'
    assert cultural_attraction.description == 'Test description'
    assert str(cultural_attraction) == cultural_attraction.title

@pytest.mark.django_db
def test_destination_model():
    cultural_attraction = CulturalAttraction.objects.create(title='Attraction', description='Test description')
    destination = Destination.objects.create(title='Destination', description='Test destination', cultural_attraction=cultural_attraction)
    destination.save()
    destination_2 = Destination.objects.create(title='Destination', description='Test destination', cultural_attraction=cultural_attraction)
    assert Destination.objects.count() == 2
    assert destination.slug != destination_2.slug
    assert destination.title == 'Destination'
    assert destination.description == 'Test destination'
    assert destination.cultural_attraction == cultural_attraction
    assert str(destination) == destination.title

@pytest.mark.django_db
def test_tour_package_model():
    destination = Destination.objects.create(title='Destination', description='Test destination')
    tour_package = TourPackage.objects.create(title='Package', description='Test package', destination=destination, price=100.00, start_date='2022-01-01', duration_days=5, duration_nights=4)
    assert tour_package.title == 'Package'
    assert str(tour_package) == tour_package.title
    assert tour_package.description == 'Test package'
    assert tour_package.destination == destination
    assert tour_package.price == 100.00
    assert tour_package.start_date == '2022-01-01'
    assert tour_package.duration_days == 5
    assert tour_package.duration_nights == 4

@pytest.mark.django_db
def test_booking_model():
    user = User.objects.create(username='testuser', phonenumber='1234567890')
    customer = Customer.objects.create(user=user)
    destination = Destination.objects.create(title='Destination', description='Test destination')
    tour_package = TourPackage.objects.create(title='Package', description='Test package', destination=destination, price=100.00, start_date='2022-01-01', duration_days=5, duration_nights=4)
    booking = Booking.objects.create(customer=customer, tour_package=tour_package, booking_date='2022-01-01', num_of_people=2)
    assert booking.customer == customer
    assert booking.tour_package == tour_package
    assert booking.booking_date == '2022-01-01'
    assert booking.num_of_people == 2
    assert str(booking) == f'{str(customer)} - {str(tour_package)}'

