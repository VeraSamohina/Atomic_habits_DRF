from rest_framework import generics

from atomichabit.models import Habit
from atomichabit.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwner


class HabitCreateAPIView(generics.CreateAPIView):
    """Представление для создания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Определяем порядок создания новой привычки.
        Присваиваем текущего пользователя в создателя привычки"""
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habit.objects.filter(user=self.request.user)


class HabitDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, редактирования и удаления отдельной привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated | IsOwner]

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """
    Представление для отображения списка привычек, имеющих статус публичных
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
