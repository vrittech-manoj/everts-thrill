# Generated by Django 4.2.6 on 2024-08-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_herosection_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herosection',
            name='position',
            field=models.CharField(choices=[('top', 'Top'), ('middle', 'Middle'), ('bottom', 'Bottom')], max_length=23),
        ),
    ]
