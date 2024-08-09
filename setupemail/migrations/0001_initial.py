# Generated by Django 4.2.6 on 2024-08-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp_server_address', models.CharField()),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField()),
                ('port', models.PositiveIntegerField()),
                ('required_authentication', models.BooleanField(default=True)),
                ('security', models.CharField(choices=[('None', 'None'), ('SSL', 'SSL'), ('TSL', 'TSL')], default='None', max_length=200)),
                ('smtp_username', models.CharField(blank=True, max_length=100, null=True)),
                ('verify_smtp_certificate', models.BooleanField(default=False)),
            ],
        ),
    ]
