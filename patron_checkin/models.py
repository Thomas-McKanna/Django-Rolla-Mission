from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import models
from django.core.files import File
from datetime import datetime
from PIL import Image as Img
from PIL import ExifTags
from PIL import JpegImagePlugin
from io import BytesIO
import uuid

from rolla_mission.storage_backends import PrivateMediaStorage


class Patron(models.Model):
    _id = models.CharField(
        max_length=127, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=127)
    birth_date = models.DateField()
    gender = models.CharField(max_length=31)
    phone = models.CharField(max_length=31)
    veteran = models.BooleanField(default=False)
    violence = models.BooleanField('fleeing violence', default=False)
    offender = models.BooleanField('sex offender', default=False)
    date_homeless = models.DateTimeField('date became homeless')
    date_profile_creation = models.DateField(
        'date profile creation', auto_now_add=True, null=True)
    city = models.CharField('city became homeless', max_length=127)
    reason = models.CharField(
        'reason in Rolla', max_length=127, null=True, blank=True)
    headshot = models.ImageField(
        null=True, blank=True, storage=PrivateMediaStorage())
    signature = models.ImageField(
        null=True, blank=True, storage=PrivateMediaStorage())
    last_checkin = models.DateTimeField('last checkin', null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        """ Rotate the headshot based on EXIF tags. """
        if self.headshot and self.headshot.readable():
            pilImage = Img.open(BytesIO(self.headshot.read()))
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            if (isinstance(pilImage, JpegImagePlugin.JpegImageFile) and
                    hasattr(pilImage, '_getexif') and
                    pilImage._getexif() is not None):
                exif = dict(pilImage._getexif().items())

                # https://exiftool.org/TagNames/EXIF.html (Orientation Tag)
                ROTATE_180 = 3
                ROTATE_90_CW = 6
                ROTATE_270_CW = 8

                if exif[orientation] == ROTATE_180:
                    pilImage = pilImage.rotate(180, expand=True)
                elif exif[orientation] == ROTATE_90_CW:
                    pilImage = pilImage.rotate(270, expand=True)
                elif exif[orientation] == ROTATE_270_CW:
                    pilImage = pilImage.rotate(90, expand=True)

                output = BytesIO()
                pilImage.save(output, format='JPEG', quality=75)
                output.seek(0)
                self.headshot = File(output, self.headshot.name)

        return super(Patron, self).save(*args, **kwargs)


class CheckIn(models.Model):
    patron_id = models.ForeignKey(Patron, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        return super(CheckIn, self).save(*args, **kwargs)

def update_last_checkin(instance):
    most_recent_checkin = CheckIn.objects.filter(patron_id=instance.patron_id._id).order_by('-date').first()
    if not most_recent_checkin:
        most_recent_checkin = None
    else:
        most_recent_checkin = most_recent_checkin.date
    Patron.objects.filter(_id=instance.patron_id._id).update(
        last_checkin=most_recent_checkin)

@receiver(post_save, sender=CheckIn)
def on_checkin_saved(sender, instance, **kwargs):
    update_last_checkin(instance)

@receiver(post_delete, sender=CheckIn)
def on_checkin_deleted(sender, instance, **kwargs):
    update_last_checkin(instance)
