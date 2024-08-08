# Generated by Django 4.2.6 on 2024-08-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
        ('holiday', '0004_holidaytrip_collection_alter_holidaytrip_activities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holidaytrip',
            name='faqs',
        ),
        migrations.AddField(
            model_name='holidaytrip',
            name='faqs',
            field=models.ManyToManyField(to='faqs.faqs'),
        ),
    ]
