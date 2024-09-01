# Generated by Django 4.2.6 on 2024-09-01 04:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_review_review_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star_rating',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
