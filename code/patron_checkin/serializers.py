from rest_framework import serializers
from patron_checkin.models import Patron

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
        fields = ['id', 'first_name', 'last_name']

class HeadshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
        fields = ['headshot']

class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patron
        fields = ['signature']