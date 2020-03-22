from django.db import models
import uuid
from datetime import datetime

from rolla_mission.storage_backends import PrivateMediaStorage


class Patron(models.Model):
    _id = models.CharField(
        max_length=127, primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=127)
    birth_date = models.DateField()
    gender = models.CharField(max_length=31)
    phone = models.CharField(max_length=31)
    veteran = models.BooleanField(default=False)
    violence = models.BooleanField('fleeing violence', default=False)
    offender = models.BooleanField('sex offender', default=False)
    time_homeless = models.CharField(max_length=127)
    city = models.CharField('city became homeless', max_length=127)
    reason = models.CharField(
        'reason in Rolla', max_length=127, null=True, blank=True)
    headshot = models.ImageField(
        null=True, blank=True, storage=PrivateMediaStorage())
    signature = models.ImageField(
        null=True, blank=True, storage=PrivateMediaStorage())

    def __str__(self):
        return f'{self.name}'


class CheckIn(models.Model):
    patron_id = models.ForeignKey(Patron, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.date)
