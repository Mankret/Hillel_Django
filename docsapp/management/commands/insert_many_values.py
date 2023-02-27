from django.core.management.base import BaseCommand

from docsapp.models import Author, Book, Publisher, Store

from faker import Faker
from faker.generator import random

fake = Faker()


class Command(BaseCommand):
    help = 'Inserts many authors and books'

    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        Book.objects.all().delete()
        Publisher.objects.all().delete()
        Store.objects.all().delete()
        index = 0
        books = []

        Publisher.objects.bulk_create(
            [
                Publisher(name=fake.company()) for _ in range(1, 6)
            ])

        for publisher in Publisher.objects.all():
            for _ in range(500):
                index = index + 1
                books.append(
                    Book(name=f'Book Test {index}', price=round(random.uniform(1, 99), 2),
                         pages=random.randint(80, 1000),
                         rating=round(random.uniform(1, 10), 1), publisher=publisher,
                         )
                )

        Book.objects.bulk_create(books)

        books = list(Book.objects.all())
        for i in range(10):
            temp_books = [books.pop(0) for i in range(250)]
            store = Store.objects.create(name=f"{fake.company()}")
            store.books.set(temp_books)
            store.save()

        books = list(Book.objects.all())
        for _ in range(500):
            temp_books = [books.pop(0) for i in range(5)]
            author = Author.objects.create(name=fake.name(), age=random.randint(20, 80))
            author.book_set.add(*temp_books)
            author.save()
