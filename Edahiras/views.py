from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Membres, Audio, Sections, Localites, Dahiras
from .serializers import MembresSerializer, DahirasSerializer, AudioSerializer, SectionsSerializer, LocalitesSerializer


# Creation d'une vue d'API
class MembresViewSet(viewsets.ModelViewSet):
    queryset = Membres.objects.all()
    serializer_class = MembresSerializer

class DahirasViewSet(viewsets.ModelViewSet):
    queryset = Dahiras.objects.all()
    serializer_class = DahirasSerializer

class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer

class LocalitesViewSet(viewsets.ModelViewSet):
    queryset = Localites.objects.all()
    serializer_class = LocalitesSerializer

