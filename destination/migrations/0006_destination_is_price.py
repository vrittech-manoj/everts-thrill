# Generated by Django 4.2.6 on 2024-08-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destination', '0005_remove_destination_activities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='is_price',
            field=models.BooleanField(default=False),
        ),
    ]
