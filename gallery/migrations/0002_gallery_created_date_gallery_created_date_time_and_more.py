# Generated by Django 4.2.6 on 2024-09-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='created_date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='updated_date_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
