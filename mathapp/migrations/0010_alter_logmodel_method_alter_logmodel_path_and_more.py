# Generated by Django 4.1.5 on 2023-02-08 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathapp', '0009_alter_logmodel_body_alter_logmodel_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmodel',
            name='method',
            field=models.CharField(default=None, max_length=120),
        ),
        migrations.AlterField(
            model_name='logmodel',
            name='path',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='logmodel',
            name='user',
            field=models.CharField(default=None, max_length=120),
        ),
    ]
