# Generated by Django 4.2.6 on 2024-09-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_contacttusdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetteam',
            name='index',
            field=models.PositiveIntegerField(default=999, unique=True),
        ),
    ]
