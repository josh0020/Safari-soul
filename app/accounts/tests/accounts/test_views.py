# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from django.test import Client
# import pytest

# User = get_user_model()

# @pytest.mark.django_db
# class TestRegisterViews:
#     def setup_method(self):
#         self.client = Client()
#         self.register_url = reverse('register')
#         self.login_url = reverse('login')
#         self.user_data = {
#             'username': 'testuser',
#             'password1': 'testpassword',
#             'password2': 'testpassword'
#         }

#     def test_register_view_get(self):
#         response = self.client.get(self.register_url)
#         assert response.status_code == 200
#         assert 'accounts/register.html' in [template.name for template in response.templates]

#     def test_register_view_post(self):
#         response = self.client.post(self.register_url, data=self.user_data)
#         assert response.status_code == 302
#         assert response.url == self.login_url

#         # Check if the user is created
#         user = User.objects.get(username=self.user_data['username'])
#         assert user.username == self.user_data['username']

# @pytest.mark.django_db
# class TestLoginViews:
#     def setup_method(self):
#         self.client = Client()
#         self.login_url = reverse('login')
#         # self.index_url = reverse('api_overview')
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

#     def test_login_view_get(self):
#         response = self.client.get(self.login_url)
#         assert response.status_code == 200
#         assert 'accounts/login_logout.html' in [template.name for template in response.templates]

#     def test_login_view_post(self):
#         response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
#         assert response.status_code == 302
#         # assert response.url == self.index_url

