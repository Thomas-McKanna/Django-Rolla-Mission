# Generated by Django 3.0.3 on 2020-03-17 03:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patron_checkin', '0006_auto_20200314_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patron',
            name='_id',
            field=models.CharField(default=uuid.UUID('69de404c-9ecf-4e72-a10e-42448a53e386'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
