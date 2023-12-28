# Generated by Django 4.0.3 on 2023-12-27 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0004_alter_race_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='distance',
            field=models.FloatField(choices=[(3.1, '5k'), (6.2, '10k'), (13.1, 'Half marathon'), (26.2, 'Marathon'), (18.6, '30k'), (21.7, '35k'), (31.1, '50k'), (50, '50 mile'), (62.1, '100k'), (100, '100 mile')]),
        ),
    ]