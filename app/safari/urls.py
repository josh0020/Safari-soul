from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CulturalAttractionViewSet, DestinationViewSet, TourPackageViewSet, CustomerViewSet, BookingViewSet, apiOverview, CulturalAttractionListView, CulturalAttractionDetailView, DestinationListView, DestinationDetailView

router = DefaultRouter()
router.register(r'cultural_attractions', CulturalAttractionViewSet, basename='cultural_attraction_set')
router.register(r'destinations', DestinationViewSet, basename='destination_set')
router.register(r'tourpackages', TourPackageViewSet, basename='tourpackage_set')
router.register(r'customers', CustomerViewSet, basename='customer_set')
router.register(r'bookings', BookingViewSet, basename='booking_set') #basename=None

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', apiOverview, name='api_overview'),
    path('v1/cultural_attractions/', CulturalAttractionListView.as_view(), name='cultural_attractions'),
    path('v1/cultural_attractions/<int:pk>', CulturalAttractionDetailView.as_view(), name='cultural_attraction'),
    path('v1/destinations/', DestinationListView.as_view(), name='destinations'),
    path('v1/destinations/<int:pk>', DestinationDetailView.as_view(), name='destination'),
]