# Generated by Django 3.2.18 on 2023-03-03 22:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_auto_20230303_2254"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="description",
            new_name="about_the_program",
        ),
        migrations.AddField(
            model_name="job",
            name="perks",
            field=models.TextField(default=" "),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="job",
            name="who_can_apply",
            field=models.TextField(default=" "),
            preserve_default=False,
        ),
    ]
