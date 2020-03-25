from patron_checkin.models import Patron, CheckIn
from api.serializers import ExtendedPatronSerializer
from api.serializers import PatronSerializer
from api.serializers import HeadshotSerializer
from api.serializers import SignatureSerializer
from api.serializers import CheckInSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework import permissions

class PatronList(generics.ListCreateAPIView):
    queryset = Patron.objects.all()
    serializer_class = ExtendedPatronSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateHeadshot(generics.RetrieveUpdateAPIView):
    queryset = Patron.objects.all()
    serializer_class = HeadshotSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateSignature(generics.RetrieveUpdateAPIView):
    queryset = Patron.objects.all()
    serializer_class = SignatureSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckInPatron(generics.CreateAPIView):
    serializer_class = CheckInSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatronSearch(generics.ListAPIView):
    serializer_class = PatronSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        name = self.kwargs['name']
        queryset = Patron.objects.filter(name__icontains=name).order_by('name')
        return queryset
