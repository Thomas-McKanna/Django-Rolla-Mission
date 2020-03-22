from rest_framework import serializers
from patron_checkin.models import Patron, CheckIn

class ExtendedPatronSerializer(serializers.ModelSerializer):
    """
    Patron serializer that contains all fields except those which are
    image-related.
    """
    class Meta:
        model = Patron
        exclude = ['headshot', 'signature']

class PatronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
        fields = ['_id', 'name']

class HeadshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
        fields = ['headshot']

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
        fields = ['signature']

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['patron_id', 'date']
