# Generated by Django 4.0.4 on 2022-05-10 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0004_alter_scan_data_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scan_data',
            options={'get_latest_by': ['number_scans']},
        ),
    ]
