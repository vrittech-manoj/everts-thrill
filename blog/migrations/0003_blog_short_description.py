# Generated by Django 4.2.6 on 2024-09-09 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_created_date_time_alter_blog_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
