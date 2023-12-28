# Generated by Django 4.0.3 on 2023-12-27 01:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("races", "0003_alter_race_distance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="race",
            name="distance",
            field=models.FloatField(
                choices=[
                    ("5k", 3.1),
                    ("10k", 6.2),
                    ("Half marathon", 13.1),
                    ("Marathon", 26.2),
                    ("30k", 18.6),
                    ("35k", 21.7),
                    ("50k", 31.1),
                    ("50 mile", 50),
                    ("100k", 62.1),
                    ("100 mile", 100),
                ]
            ),
        ),
    ]
