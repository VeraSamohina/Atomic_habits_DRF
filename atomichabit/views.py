from rest_framework import generics

from atomichabit.models import Habit
from atomichabit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Представление для создания привычки"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """ Определяем порядок создания новой привычки
        Присваиваем текущего пользователя в создателя привычки"""
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habit.objects.filter(user=self.request.user)

class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Представление для просмотра, редактирования и удаления отдельной привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habit.objects.filter(user=self.request.user)