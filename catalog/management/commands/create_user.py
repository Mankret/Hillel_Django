from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Create random user'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of created users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        if 0 < total <= 10:
            for i in range(total):
                User.objects.bulk_create([
                    User(username=fake.name(), email=fake.email(), password=get_random_string(10))
                ])
            self.stdout.write(
               self.style.SUCCESS('Users successfully added'))
        else:
            raise CommandError(f"Invalid value: {total}")
