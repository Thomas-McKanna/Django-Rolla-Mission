from django.db import models
import uuid
from datetime import datetime

from rolla_mission.storage_backends import PrivateMediaStorage

class Patron(models.Model):
    headshot = models.ImageField(null=True, blank=True, storage=PrivateMediaStorage())
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    veteran = models.BooleanField(default=False)
    violence = models.BooleanField('fleeing violence', default=False)
    offender = models.BooleanField('sex offender', default=False)
    date_homeless = models.DateTimeField()
    city = models.CharField('city became homeless', max_length=70)
    reason = models.CharField('reason in Rolla', max_length=20, null=True, blank=True)
    other = models.CharField('other reason', max_length=200, null=True, blank=True)    
    headshot = models.ImageField(null=True, blank=True, storage=PrivateMediaStorage())
    signature = models.ImageField(null=True, blank=True, storage=PrivateMediaStorage())

    _id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4())

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class CheckIn(models.Model):
    patron_id = models.ForeignKey(Patron, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.date
