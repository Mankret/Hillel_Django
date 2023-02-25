from bs4 import BeautifulSoup

from celery import shared_task

from celery_beat_parsing.models import Author, Quotes

from django.core.mail import send_mail

import requests


@shared_task
def sending_mail(email, message):
    send_mail(
        'Reminder',
        f'{message}',
        'admin@admin.com',
        [email]
    )
    return 'Done'


@shared_task()
def parser_five_new_quotes():
    page = 0
    quote_list = []
    while True:
        page += 1
        base_url = f'http://quotes.toscrape.com/page/{page}'
        req = requests.get(base_url)
        soup = BeautifulSoup(req.content, 'html.parser')
        quotes_all = soup.find_all('div', {'class': 'quote'})
        for quotes in quotes_all:
            authors = quotes.find('small', {'class': 'author'}).text
            links_detail = quotes.find('a')['href']
            link_detail = f'http://quotes.toscrape.com/{links_detail}'
            rek = requests.get(link_detail)
            if not Author.objects.filter(name=authors).exists():
                authors_detail = BeautifulSoup(rek.content, 'html.parser')
                author_detail = authors_detail.find_all('div', {'class': 'author-details'})
                for detail in author_detail:
                    author_dates = detail.find('span', {'class': 'author-born-date'}).text
                    author_locations = detail.find('span', {'class': 'author-born-location'}).text
                    author_description = detail.find('div', {'class': 'author-description'}).text
                author = Author.objects.create(name=authors, born=f'{author_dates}' + f'{author_locations}',
                                               description=author_description)
                author.save()
            else:
                author = Author.objects.get(name=authors)
            quote = quotes.find('span', {'class': 'text'}).text
            quote_exist = Quotes.objects.filter(quote=quote).exists()
            if not quote_exist:
                quote_list.append(Quotes(quote=quote, author=author))
            if len(quote_list) == 5:
                break
        if page > 10:
            send_mail(
                'OK',
                'There is no more quote',
                'admin@admin.com',
                ['admin@admin.com']
            )
        else:
            continue

        Quotes.objects.bulk_create(quote_list)
        break
