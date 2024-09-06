# Generated by Django 4.2.6 on 2024-09-05 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('destination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upcoming_departure_date', models.DateTimeField(blank=True, null=True)),
                ('upcoming_departure_status', models.BooleanField(blank=True, default=False, null=True)),
                ('upcoming_departure_price', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('destination_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_departures', to='destination.destination')),
            ],
        ),
    ]
