from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APITestCase

from ..models import User


class LoginTest(APITestCase):
    "Test case for login "

    url = reverse('login')

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_authentication_without_password(self):
        response = self.client.post(self.url, {"username": "snowman"})
        self.assertEqual(400, response.status_code)
   
