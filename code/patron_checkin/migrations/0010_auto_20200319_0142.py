# Generated by Django 3.0.3 on 2020-03-19 06:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('patron_checkin', '0009_auto_20200319_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patron',
            name='_id',
            field=models.CharField(default=uuid.UUID('d93e4888-7f56-4eee-a959-38083b963084'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
