# Generated by Django 5.1.7 on 2025-04-07 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_bookingdate_alter_booking_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='bookingdate',
            new_name='booking_date',
        ),
    ]
