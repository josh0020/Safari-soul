import pytest
from accounts.models import User, UserProfile

@pytest.mark.django_db
class TestUserModel:
    def setup_method(self):
        # Set up any necessary data for the tests
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'phonenumber': '1234567890',
        }

    def test_user_creation(self):
        # Test user creation
        user = User.objects.create_user(**self.user_data)
        assert user.username == self.user_data['username']
        assert user.email == self.user_data['email']
        assert user.phonenumber == self.user_data['phonenumber']

    def test_user_string_representation(self):
        # Test user string representation
        user = User.objects.create_user(**self.user_data)
        assert str(user) == self.user_data['username']

    def test_user_profile(self):
        # Test user profile and the str representation of UserProfile model
        user = User.objects.create_user(**self.user_data)
        # create profile using signal
        profile = user.userprofile
        assert profile.user == user
        assert str(profile) == f"{user.username}'s Profile"
        

