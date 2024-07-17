from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin',
            first_name='Admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()