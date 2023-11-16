from rest_framework import serializers

from atomichabit.models import Habit
from atomichabit.validators import HabitTimeValidator, HabitRewardValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор для модели привычки"""
    validators = [HabitTimeValidator(field='execute_time'),
                  HabitRewardValidator(reward='reward', connect_habit='connect_habit', is_nice='is_nice', user='user')]

    class Meta:
        model = Habit
        exclude = ('user',)
