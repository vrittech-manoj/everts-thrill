# Generated by Django 4.2.6 on 2024-08-09 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqs',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
