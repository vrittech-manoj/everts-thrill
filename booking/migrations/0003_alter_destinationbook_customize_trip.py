# Generated by Django 4.2.6 on 2024-09-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_destinationbook_created_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationbook',
            name='customize_trip',
            field=models.CharField(blank=True, null=True),
        ),
    ]
