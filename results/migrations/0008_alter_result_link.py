# Generated by Django 4.0.3 on 2023-12-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("results", "0007_result_hours_result_minutes_result_seconds"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
