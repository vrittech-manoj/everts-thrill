# Generated by Django 4.2.6 on 2024-08-16 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_collection_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='featured_image',
        ),
    ]
