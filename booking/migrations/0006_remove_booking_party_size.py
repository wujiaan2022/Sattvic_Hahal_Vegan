# Generated by Django 3.2.20 on 2023-08-20 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='party_size',
        ),
    ]
