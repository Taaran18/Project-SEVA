# Generated by Django 3.2.18 on 2023-03-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_appliedjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjob',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]