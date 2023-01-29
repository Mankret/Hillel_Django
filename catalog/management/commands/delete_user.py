from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']
        superuser = User.objects.filter(is_superuser=True)
        users = User.objects.filter(id__in=users_ids)

        if users.filter(id__in=superuser).exists():
            self.stdout.write(self.style.WARNING("Can't delete superuser"))
        else:
            users.delete()

