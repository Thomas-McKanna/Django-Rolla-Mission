# Generated by Django 3.0.3 on 2020-03-06 02:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patron_checkin', '0005_auto_20200305_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patron',
            name='_id',
            field=models.CharField(default=uuid.UUID('40c2f39a-5a3a-4029-a2aa-8b32d6fb2cb8'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
