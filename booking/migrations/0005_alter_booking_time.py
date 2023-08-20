# Generated by Django 3.2.20 on 2023-08-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(choices=[('12:00 for Lunch', '12:00 Lunch Time'), ('18:00 for Dinner', '18:00 Dinner Time')], max_length=20),
        ),
    ]