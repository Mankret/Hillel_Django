from celery import shared_task

from django.core.mail import send_mail
from django.utils import timezone


@shared_task
def sending_mail(email, message):
    send_mail(
        'Reminder',
        f'{message}',
        'admin@admin.com',
        [email]
    )
    return 'Done'
