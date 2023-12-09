from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserApiViewTest(APITestCase):

    def setUp(self):
        # Тестовый пользователь
        self.user = User.objects.create(email="userbefore@example.com", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_registration(self):
        """"""
        data = {
            "email": "testuser@example.com",
            "password": "testpassword",
        }
        response = self.client.post(reverse('users:user-create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['email'], 'testuser@example.com')

    def test_update(self):

        data = {
            'email': 'userafter@example.com'}

        response = self.client.patch(reverse('users:user-update', args=[self.user.id]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['email'], 'userafter@example.com')
