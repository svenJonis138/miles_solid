# Generated by Django 2.2.5 on 2019-09-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miles_app', '0003_auto_20190923_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miles',
            name='id',
        ),
        migrations.AlterField(
            model_name='miles',
            name='vehicle',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
