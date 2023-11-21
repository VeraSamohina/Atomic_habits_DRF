from django.conf import settings
from django.db import models


class Habit(models.Model):
    """
    Модель, представляющая собой привычку пользователя.

    Поля:
    - user (ForeignKey): Пользователь, создавший привычку.
    - place (CharField): Место, в котором необходимо выполнять привычку.
    - time (TimeField): Время, когда необходимо выполнять привычку.
    - action (CharField): Непосредственное действие - привычка.
    - is_nice(BooleanField): Признак приятной привычки.
    - connected_habit (ForeignKey): Связанная привычка, если есть.
    - periodicity (CharField): Периодичность выполнения привычки для напоминания в днях.
    - weekday (CharField): Старт выполнения привычки.
    - reward (CharField): Вознаграждение за выполнение привычки.
    - execute_time (PositiveSmallIntegerField): Время  на выполнение привычки.
    - is_public (BooleanField): Признак публичности привычки.
    - date_add (DateField): Дата добавления привычки
    """

    class Periodicity(models.TextChoices):
        DAILY = "DAILY", "ежедневно"
        WEEKLY = "WEEKLY", "еженедельно"
        WEEKDAYS = "WEEKDAYS", "по будням"
        WEEKENDS = "WEEKENDS", "по выходным"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=150, default='везде', verbose_name='место')
    habit_time = models.TimeField(verbose_name='время')
    habit_action = models.CharField(max_length=255, verbose_name='действие')
    periodicity = models.CharField(choices=Periodicity.choices, default='DAILY', verbose_name='периодичность')
    is_nice = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    connect_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', null=True,
                                      blank=True)
    reward = models.CharField(max_length=1000, verbose_name='вознаграждение', null=True, blank=True)
    execute_time = models.PositiveSmallIntegerField(verbose_name='время выполнения')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        """
        Возвращает строку, описывающую привычку.

        Returns:
            str: Строка с описанием привычки.
        """
        return f'Я буду {self.habit_action} в {self.habit_time}  {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
