# Generated by Django 4.1.5 on 2023-02-08 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathapp', '0006_logmodel_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logmodel',
            old_name='data',
            new_name='body',
        ),
        migrations.AddField(
            model_name='logmodel',
            name='query',
            field=models.TextField(null=True),
        ),
    ]
