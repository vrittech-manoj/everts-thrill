# Generated by Django 4.2.6 on 2024-09-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_destinationbook_activity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationbook',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
