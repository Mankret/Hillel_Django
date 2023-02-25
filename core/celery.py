import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'quotes-parser': {
            'task': 'docsapp.task.parser_five_new_quotes',
            'schedule': crontab(minute=0, hour='1-23/2')
    },
}
