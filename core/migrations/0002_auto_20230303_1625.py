# Generated by Django 3.2.18 on 2023-03-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=122)),
                ("email", models.CharField(max_length=122)),
                ("phone", models.CharField(max_length=12)),
                ("desc", models.TextField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name="OrganizationUser",
        ),
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="designation",
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="domain",
            field=models.CharField(
                choices=[
                    ("All", "All"),
                    ("Aerospace and Aviation Sector", "Aerospace and Aviation Sector"),
                    ("Agriculture", "Agriculture"),
                    (
                        "Apparel Made-Ups &amp; Home Furnishing Sector",
                        "Apparel Made-Ups &amp; Home Furnishing Sector",
                    ),
                    (
                        "Automotive Skills Development Council",
                        "Automotive Skills Development Council",
                    ),
                    ("Banking", "Banking"),
                    ("Beauty &amp; Wellness Sector", "Beauty &amp; Wellness Sector"),
                    ("BFSI Sector", "BFSI Sector"),
                    ("Capital Goods", "Capital Goods"),
                    (
                        "Construction Skill Development Council",
                        "Construction Skill Development Council",
                    ),
                    ("Domestic Workers Sector", "Domestic Workers Sector"),
                    (
                        "Electronics Sector Skills Council",
                        "Electronics Sector Skills Council",
                    ),
                    ("Education and Edutech", "Education and Edutech"),
                    ("Tourism and Hospitality", "Tourism and Hospitality"),
                    (
                        "Food Industry Capacity &amp; Skill Initiative",
                        "Food Industry Capacity &amp; Skill Initiative",
                    ),
                    ("Furniture &amp; Fittings", "Furniture &amp; Fittings"),
                    ("Gem &amp; Jewellery", "Gem &amp; Jewellery"),
                    ("Handicrafts and Carpet Sector", "Handicrafts and Carpet Sector"),
                    ("Healthcare Sector", "Healthcare Sector"),
                    ("Hydrocarbon Sector", "Hydrocarbon Sector"),
                    ("Indian Iron and Steel Sector", "Indian Iron and Steel Sector"),
                    (
                        "Indian Plumbing Skills council",
                        "Indian Plumbing Skills council",
                    ),
                    ("Infrastructure Equipment", "Infrastructure Equipment"),
                    ("IT-ITeS Sector", "IT-ITeS Sector"),
                    ("Leather Sector", "Leather Sector"),
                    (
                        "Life Sciences Sector Skill Development Council",
                        "Life Sciences Sector Skill Development Council",
                    ),
                    ("Logistics Sector", "Logistics Sector"),
                    (
                        "Management &amp; Entrepreneurship and Professional Skills Council (MEPSC)",
                        "Management &amp; Entrepreneurship and Professional Skills Council (MEPSC)",
                    ),
                    ("Media &amp; Entertainment", "Media &amp; Entertainment"),
                    ("Paints and Coatings", "Paints and Coatings"),
                    ("Power Sector", "Power Sector"),
                    ("Retailers Association's", "Retailers Association's"),
                    (
                        "Rubber Skill Development Council",
                        "Rubber Skill Development Council",
                    ),
                    ("Green Jobs", "Green Jobs"),
                    ("Mining Sector", "Mining Sector"),
                    ("Persons with Disability", "Persons with Disability"),
                    (
                        "Sports, Physical Education, Fitness &amp; Leisure Skills Council",
                        "Sports, Physical Education, Fitness &amp; Leisure Skills Council",
                    ),
                    ("Telecom Sector ", "Telecom Sector "),
                    ("Textile Sector", "Textile Sector"),
                    ("Tourism and Hospitality", "Tourism and Hospitality"),
                ],
                default="All",
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="mobile",
            field=models.BigIntegerField(default="84848"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="organisation_name",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="photo",
            field=models.ImageField(default=None, upload_to="images"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="skills",
            field=models.TextField(
                default=None,
                help_text="Enter your skills separated by comma: skill1, skill2",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="state",
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                choices=[("organisation", "organisation"), ("normal", "normal")],
                default="normal",
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
