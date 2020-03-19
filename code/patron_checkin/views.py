from patron_checkin.models import Patron
from patron_checkin.serializers import PatronSerializer
from patron_checkin.serializers import ExtendedPatronSerializer
from patron_checkin.serializers import HeadshotSerializer
from patron_checkin.serializers import SignatureSerializer
from rest_framework import generics
from rest_framework import filters
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


class PatronSearch(generics.ListCreateAPIView):
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer

