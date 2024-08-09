# Generated by Django 4.2.6 on 2024-08-09 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('destination', '__first__'),
        ('services', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_price', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField(default=0)),
                ('desired_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_book', to='services.services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_book', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('country', models.CharField(max_length=45)),
                ('airlines', models.CharField(max_length=45)),
                ('number_of_travellers', models.IntegerField(default=1)),
                ('arrival_date', models.DateTimeField()),
                ('departure_date', models.DateTimeField()),
                ('service_type', models.CharField(choices=[('budget', 'Budget'), ('standard', 'Standard'), ('premium', 'Premium')], max_length=20)),
                ('customize_trip', models.CharField(max_length=450)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_booking', to='activities.activity')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_book', to='destination.destination')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package_booking', to='destination.package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
