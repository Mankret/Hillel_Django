# Generated by Django 4.1.5 on 2023-02-08 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathapp', '0010_alter_logmodel_method_alter_logmodel_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logmodel',
            name='body',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='logmodel',
            name='method',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='logmodel',
            name='path',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='logmodel',
            name='query',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='logmodel',
            name='user',
            field=models.CharField(max_length=120),
        ),
    ]