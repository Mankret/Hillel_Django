# Generated by Django 4.1.5 on 2023-02-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathapp', '0002_alter_person_first_name_alter_person_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(default=None, max_length=200)),
                ('method', models.CharField(max_length=120)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('data', models.TextField()),
                ('user', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
