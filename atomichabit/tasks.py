from datetime import datetime
import requests
from celery import shared_task
from django.conf import settings

from atomichabit.models import Habit
from atomichabit.services import is_day_habit

token = settings.BOT_TOKEN


@shared_task
def send_reminder():
    """
    Отправка напоминания о привычке
    """
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    current_time = datetime.now().time().replace(second=0, microsecond=0)
    habits = Habit.objects.filter(is_nice=False)
    for habit in habits:
        if habit.habit_time.replace(second=0, microsecond=0) == current_time:
            if habit.user.chat_id != 0 and is_day_habit(habit_id=habit.id):
                print(f'отправка уведомления для {habit.user}')
                params = {'chat_id': habit.user.chat_id, 'text': f'Напоминание: пришло время {habit.habit_action}'}
                response = requests.post(url, params=params)
                if response.status_code == 200:
                    print('Уведомление отправлено')
                else:
                    print('Уведомление не отправлено')
