# Generated by Django 3.0.3 on 2020-03-04 01:38

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=70, verbose_name='city became homeless')),
                ('reason', models.CharField(max_length=20, verbose_name='reason in rolla')),
                ('other', models.CharField(blank=True, max_length=20, null=True, verbose_name='other reason')),
                ('time_homeless', models.CharField(max_length=70)),
                ('veteran', models.BooleanField(default=False)),
                ('violence', models.BooleanField(default=False, verbose_name='fleeing violence')),
                ('offender', models.BooleanField(default=False, verbose_name='sex offender')),
                ('_id', models.CharField(default=uuid.UUID('ebe17c15-f60d-4474-84a8-58fc529fe5c3'), max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('patron_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patron_checkin.Patron')),
            ],
        ),
    ]