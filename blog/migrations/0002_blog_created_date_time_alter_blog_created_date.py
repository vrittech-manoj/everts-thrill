# Generated by Django 4.2.6 on 2024-09-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
