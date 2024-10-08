# Generated by Django 4.2.6 on 2024-09-05 09:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('destination_title', models.CharField(max_length=70, unique=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('price_type', models.CharField(default='USD', max_length=3)),
                ('is_price', models.BooleanField(default=False)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='destination/featured/images/')),
                ('overview', models.CharField(blank=True, max_length=5000, null=True)),
                ('inclusion_and_exclusion', models.TextField(blank=True, default='', null=True)),
                ('ltinerary', models.TextField()),
                ('trip_map_url', models.URLField(blank=True, null=True)),
                ('trip_map_image', models.ImageField(blank=True, null=True, upload_to='destination/trip-map/images/')),
                ('gear_and_equipment', models.TextField(blank=True, default='', null=True)),
                ('useful_information', models.TextField(blank=True, default='', null=True)),
                ('duration', models.PositiveIntegerField()),
                ('trip_grade', models.CharField(max_length=150)),
                ('best_season', models.CharField(blank=True, max_length=150, null=True)),
                ('max_altitude', models.CharField(max_length=150)),
                ('meals', models.CharField(max_length=150)),
                ('nature_of_trip', models.CharField(max_length=150)),
                ('accommodation', models.CharField(max_length=150)),
                ('group_size', models.CharField(max_length=70)),
                ('meta_title', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('name', models.CharField(max_length=400, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='destination/package_image/')),
            ],
        ),
        migrations.CreateModel(
            name='DestinationReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField(default=1, help_text='Enter a number less than 5 stars', validators=[django.core.validators.MaxValueValidator(5)])),
                ('comments', models.CharField(max_length=2000)),
                ('destination_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='destination.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationGalleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='destination/images/')),
                ('destination_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleryimages', to='destination.destination')),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='packages',
            field=models.ManyToManyField(to='destination.package'),
        ),
    ]
