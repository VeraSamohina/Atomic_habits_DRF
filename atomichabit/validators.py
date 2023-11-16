from rest_framework.serializers import ValidationError


class HabitTimeValidator:
    """ Валидатор для поля времени выполнения привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Возбуждается
        ValidationError если время выполнения привычки более 120 секунд"""

        execute_time = value.get(self.field)
        if execute_time and execute_time > 120:
            raise ValidationError('Время выполнения привычки должно быть не больше 120 секунд')


class HabitRewardValidator:
    """ Валидатор для поля вознаграждения и связанной привычки(СП)"""

    def __init__(self, reward, connect_habit, is_nice, user):
        self.reward = reward
        self.related_habit = connect_habit
        self.is_nice = is_nice
        self.user = user

    def __call__(self, value):
        """

        Возбуждается ValidationError если:
        - у приятной привычки есть СП или вознаграждение;
        - у обычной привычки выбрано и вознаграждение и СП или не выбрано ни одного поля;
        - СП не имеет признак приятной
        - в СП добавляют привычку, созданную не текущим пользователем
        """
        reward = value.get(self.reward)
        connect_habit = value.get(self.related_habit)
        user = value.get(self.user)

        if value.get(self.is_nice):
            if reward or connect_habit:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
        elif reward and connect_habit:
            raise ValidationError('Нельзя выбрать одновременно связанную привычку вознаграждение')
        elif not reward and not connect_habit:
            raise ValidationError('Нужно выбрать связанную привычку или вознаграждение')
        elif connect_habit and not connect_habit.is_nice:
            raise ValidationError('Связанная привычка должна иметь признак приятной привычки')
        elif connect_habit and connect_habit.user != user:
            raise ValidationError('Вы не можете использовать привычки, '
                                  'созданные другими пользователями, в качестве связанных ')
