
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели пользователя.

        Attributes:
        id (int): Уникальный идентификатор пользователя.
        email (str): Адрес электронной почты пользователя.
        first_name (str): Имя пользователя.
        last_name (str): Фамилия пользователя.
        avatar (str): Путь к изображению профиля пользователя.
        phone (str): Номер телефона пользователя.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar', 'phone']


class UserRegisterSerializer(serializers.ModelSerializer):
    """
        Сериализатор для модели пользователя для регистрации.
    """
    class Meta:
        model = User
        fields = '__all__'


