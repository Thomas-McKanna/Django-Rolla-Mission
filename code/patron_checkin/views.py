from patron_checkin.models import Patron
from patron_checkin.serializers import ExtendedPatronSerializer
from patron_checkin.serializers import HeadshotSerializer
from patron_checkin.serializers import SignatureSerializer
from patron_checkin.serializers import CheckInSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser


class PatronList(generics.ListCreateAPIView):
    queryset = Patron.objects.all()
    serializer_class = ExtendedPatronSerializer


class UpdateHeadshot(generics.RetrieveUpdateAPIView):
    queryset = Patron.objects.all()
    serializer_class = HeadshotSerializer


class UpdateSignature(generics.RetrieveUpdateAPIView):
    queryset = Patron.objects.all()
    serializer_class = SignatureSerializer

class CheckInPatron(generics.CreateAPIView):
    serializer_class = CheckInSerializer