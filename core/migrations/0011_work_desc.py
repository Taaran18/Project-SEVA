# Generated by Django 3.2.18 on 2023-03-04 01:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_auto_20230304_0629"),
    ]

    operations = [
        migrations.AddField(
            model_name="work",
            name="desc",
            field=models.CharField(default="SIJinjn  osuid ufdsuo ", max_length=255),
            preserve_default=False,
        ),
    ]
