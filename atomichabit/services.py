from datetime import datetime

from django.conf import settings

from atomichabit.models import Habit

token = settings.BOT_TOKEN
current_day = datetime.now().today()


def is_day_habit(habit_id):
    habit = Habit.objects.get(pk=habit_id)
    print(habit.periodicity)
    if habit.periodicity == 'DAILY':
        return True
    elif habit.periodicity == 'WEEKLY' and habit.date_add.weekday() == current_day.weekday():
        return True
    elif habit.periodicity == 'WEEKDAYS' and current_day.weekday() not in [5, 6]:
        return True
    elif habit.periodicity == 'WEEKENDS' and current_day.weekday() in [5, 6]:
        return True
    else:
        return False
