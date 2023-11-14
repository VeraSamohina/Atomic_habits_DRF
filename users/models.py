from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
            Переопределяем стандартную модель пользователя.
            Добавляем авторизацию по email и расширяем модель дополнительной информацией:
            номер телефона, аватар, chat_id (для уведомлений в телеграмм)

            Attributes:
                email (str): Уникальный адрес электронной почты пользователя.
                avatar (ImageField): Изображение профиля пользователя.
                phone (str): Номер телефона пользователя.
                chat_id(str): Id чата в tg
        """
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name='Аватар')
    phone = models.CharField(max_length=35, null=True, blank=True, verbose_name='Телефон')
    chat_id = models.CharField(max_length=20, default=0, verbose_name='ID чата в tg')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
