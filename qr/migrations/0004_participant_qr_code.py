# Generated by Django 4.0.4 on 2022-05-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0003_remove_participant_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='qr_code',
            field=models.ImageField(default='upload/', upload_to=''),
        ),
    ]
