# Generated by Django 4.2.6 on 2024-09-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_read_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_by',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
