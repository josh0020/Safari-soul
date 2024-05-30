from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'phonenumber')  # Add any additional fields you want to include in the registration form
