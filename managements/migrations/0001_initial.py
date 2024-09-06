# Generated by Django 4.2.6 on 2024-09-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, default='', max_length=150)),
                ('email', models.CharField(blank=True, default='', max_length=150)),
                ('teliphone', models.CharField(blank=True, default='', max_length=150)),
                ('contact_info', models.CharField(blank=True, default='', max_length=150)),
                ('description', models.CharField(blank=True, default='', max_length=150)),
                ('facebook', models.CharField(blank=True, default='', max_length=150)),
                ('twitter', models.CharField(blank=True, default='', max_length=150)),
                ('youtube', models.CharField(blank=True, default='', max_length=150)),
                ('site_icon', models.ImageField(blank=True, null=True, upload_to='site/images')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='site/images')),
                ('site_title', models.CharField(blank=True, default='', max_length=150)),
                ('site_name', models.CharField(blank=True, default='', max_length=150)),
            ],
        ),
    ]
