# Generated by Django 4.2.6 on 2024-09-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departure', '0002_departure_created_date_departure_created_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='upcoming_departure_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
