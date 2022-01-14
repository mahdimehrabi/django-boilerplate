from django.test import TestCase
from django.test.client import Client
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTest(TestCase):
    def setUp(self) -> None:
        self.superuser = User.objects.create_superuser(
            'myuser', 'myemail@test.com', 'password123')
        self.client = Client()
        self.client.force_login(self.superuser)
        self.create_data()
        return super().setUp()

    def create_data(self):
        pass

    def test_ok(self):
        self.assertTrue(True)
