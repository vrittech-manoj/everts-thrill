# Generated by Django 4.2.6 on 2024-09-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinationbook',
            name='created_date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='destinationbook',
            name='arrival_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='destinationbook',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='destinationbook',
            name='departure_date',
            field=models.DateField(),
        ),
    ]
