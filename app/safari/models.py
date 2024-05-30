from django.db import models
from django.utils.text import slugify
from accounts.models import User
import uuid

#customer model inherits from User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"{self.user.first_name} {self.user.last_name}"
        return f"{self.user}"

# Cultural Hightlights Model
class CulturalAttraction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cultural_attraction/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Destination Model it can have a cultural artifact, created at, updated at
class Destination(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    cultural_attraction = models.ForeignKey(CulturalAttraction, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)

        if Destination.objects.filter(slug=base_slug).exists():
            self.slug = f"{base_slug}-{str(uuid.uuid4())[:4]}"
        else:
            self.slug = slugify(self.title)
        super(Destination, self).save(*args, **kwargs)

# tour packahe Model, will include a destination, price, start date , end date 
class TourPackage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    start_date = models.DateField()
    duration_days = models.PositiveIntegerField(null=True)
    duration_nights = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# booking model customer, tour package, booking date, number of people
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, blank=True, null=True)
    booking_date = models.DateField()
    num_of_people = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer} - {self.tour_package}"
