# Generated by Django 4.2.6 on 2024-08-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_rename_show_review_is_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_type',
            field=models.CharField(choices=[('destination', 'Destination'), ('company', 'Company')], default='company', max_length=20),
        ),
    ]
