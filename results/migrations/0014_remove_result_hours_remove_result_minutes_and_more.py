# Generated by Django 4.0.3 on 2023-12-28 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0013_alter_result_hours_alter_result_minutes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='hours',
        ),
        migrations.RemoveField(
            model_name='result',
            name='minutes',
        ),
        migrations.RemoveField(
            model_name='result',
            name='seconds',
        ),
    ]