# Generated by Django 3.2.20 on 2023-08-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_table_table_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.CharField(max_length=20),
        ),
    ]
