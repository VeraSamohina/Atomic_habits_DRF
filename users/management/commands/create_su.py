from django.conf import settings
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """Создает
        суперпользователя (админа)
        """
        User.objects.all().delete()

        super_user = User.objects.create(
            email='admin@mail.ru',
            first_name='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        super_user.set_password(settings.SUPERUSER_PASSWORD)
        super_user.save()
