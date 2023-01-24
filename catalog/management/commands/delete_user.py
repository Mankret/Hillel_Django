import sys

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Delete users'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']
        superuser = User.objects.get(is_superuser=True)
        if superuser.id in users_ids:
            sys.exit(f"Can't delete superuser: {superuser}, id: {superuser.id}")

        try:
            users = list(map(lambda x: User.objects.get(pk=x).delete(), users_ids))
            self.stdout.write(
                self.style.SUCCESS('Users successfully removed'))
        except User.DoesNotExist as Error:
            self.stdout.write(self.style.WARNING(f'{Error}'))
