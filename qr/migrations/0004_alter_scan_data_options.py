# Generated by Django 4.0.4 on 2022-05-10 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0003_alter_scan_data_last_scan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scan_data',
            options={'ordering': ('number_scans',)},
        ),
    ]
