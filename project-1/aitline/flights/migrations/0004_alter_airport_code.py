# Generated by Django 5.0.4 on 2024-05-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_alter_flight_destination_alter_flight_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]
