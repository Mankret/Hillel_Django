# Generated by Django 4.1.5 on 2023-02-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_beat_parsing', '0002_alter_quotes_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='quote',
            field=models.TextField(),
        ),
    ]
