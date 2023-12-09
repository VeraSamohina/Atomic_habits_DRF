from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from atomichabit.models import Habit

from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        # Тестовый пользователь
        self.user = User.objects.create(email="testuser@example.com", password="testpassword")
        self.client.force_authenticate(user=self.user)

        # Тестовая привычка
        self.habit = Habit.objects.create(
            user=self.user,
            place="setUp место",
            habit_time="10:00:00",
            habit_action="SetUp действие",
            execute_time=60,
            reward="SetUp награда")

        # Тестовая связанная привычка
        self.nice_habit = Habit.objects.create(
            user=self.user,
            place="setUp место ПП",
            habit_time="10:00:00",
            habit_action="SetUp действие ПП",
            execute_time=60,
            is_nice=True)

    def test_create_habit(self):
        """Тестирование создание привычки"""
        data = {
            "place": "Тестовое место",
            "habit_time": "10:00",
            "habit_action": "Тестовое действие",
            "execute_time": 60,
            "reward": "тестовая награда",
        }

        response = self.client.post(reverse('habits:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['habit_action'], 'Тестовое действие')

    def test_create_nice_habit(self):
        """Тестирование создание связанной привычки"""
        data = {
            "place": "место приятной привычки",
            "habit_time": "09:00",
            "habit_action": "действие приятной привычки",
            "execute_time": 60,
            "is_nice": True,
        }
        response = self.client.post(reverse('habits:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['habit_action'], 'действие приятной привычки')

    def test_create_nice_habit_error(self):
        """Тестирование ошибки при создании связанной привычки с вознаграждением"""
        data = {
            "place": "место приятной привычки",
            "habit_time": "09:00",
            "habit_action": "действие приятной привычки",
            "execute_time": 60,
            "is_nice": True,
            "reward": "тестовое вознаграждение"
        }
        response = self.client.post(reverse('habits:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_habit_without_reward(self):
        """Тестирование ошибки при создании привычки без указания вознаграждений"""
        data = {
            "place": "Тестовое место",
            "habit_time": "08:00",
            "habit_action": "Тестовое действие",
            "execute_time": 60,
        }
        response = self.client.post(reverse('habits:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_habit_with_2reward(self):
        """Тестирование ошибки при создании привычки и с вознаграждением и со связанной привычкой"""
        data = {
            "place": "Тестовое место",
            "habit_time": "08:00",
            "habit_action": "Тестовое действие",
            "execute_time": 60,
            "reward": "тестовая награда",
            "connect_habit": self.nice_habit
        }
        response = self.client.post(reverse('habits:habit-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_list(self):
        response = self.client.get(reverse('habits:habit-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        data = {
            "place": "Тестовое исправленное место",
            "reward": "тестовая награда",
        }
        response = self.client.patch(reverse('habits:habit-update', args=[self.habit.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['place'], 'Тестовое исправленное место')

    def test_delete_habit(self):
        response = self.client.delete(reverse('habits:habit-delete', args=[self.habit.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())
