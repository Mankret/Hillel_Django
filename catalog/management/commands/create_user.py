from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Create random user'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 10+1), help='Number of created users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']

        User.objects.bulk_create([
            User(username=fake.name(), email=fake.email(), password=make_password(fake.password())) for _ in
            range(total)
        ])
        self.stdout.write(
            self.style.SUCCESS('Users successfully added'))

