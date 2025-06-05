import os
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
from rest_framework import viewsets
from .models import Membres, Audio, Sections, Localites, Dahiras, Sequence, Chapitre, Theme
from .serializers import MembresSerializer, DahirasSerializer, AudioSerializer, SectionsSerializer, LocalitesSerializer, \
    SequenceSerializer, ChapitreSerializer, ThemeSerializer
from django.http import FileResponse, Http404
from rest_framework import generics
from .models import Audio
from .serializers import AudioSerializer
from .filters import AudioFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F

from django.db import models  # 👈 nécessaire pour utiliser models.F

#Crée une vue spéciale pour servir les fichiers audio (avec le bon header)
def serve_audio_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'audio', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
    else:
        raise Http404("Fichier audio non trouvé")

# Contrôler les permissions dans chaque ViewSet (facultatif)
# Si tu veux par exemple rendre /api/membres/ privée, mais laisser /api/localites/ publique, tu peux faire ça dans chaque ViewSet :
# Creation d'une vue d'API
class MembresViewSet(viewsets.ModelViewSet):
    queryset = Membres.objects.all()
    serializer_class = MembresSerializer
    #permission_classes = [IsAuthenticated]

class DahirasViewSet(viewsets.ModelViewSet):
    queryset = Dahiras.objects.all()
    serializer_class = DahirasSerializer
    #permission_classes = [IsAuthenticated]

class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all()
    serializer_class = SequenceSerializer

class ChapitreViewSet(viewsets.ModelViewSet):
    queryset = Chapitre.objects.all()
    serializer_class = ChapitreSerializer

class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


from django_filters.rest_framework import DjangoFilterBackend
from .filters import AudioFilter

class AudioViewSet(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    queryset = Audio.objects.all()  # Obligatoire pour DRF

    def get_queryset(self):
        # Par défaut, filtre tous les audios dont l’auteur == chapitre.auteur
        queryset = Audio.objects.filter(auteur=F('chapitre__auteur'))

        # Récupération des éventuels filtres GET
        chapitre_id = self.request.query_params.get('chapitre')
        if chapitre_id:
            queryset = queryset.filter(chapitre__id=chapitre_id)

        return queryset



class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer
    #permission_classes = [IsAuthenticated]

class LocalitesViewSet(viewsets.ModelViewSet):
    queryset = Localites.objects.all()
    serializer_class = LocalitesSerializer
    #permission_classes = [IsAuthenticated]




class ChapitresByThemeAPIView(generics.ListAPIView):
    serializer_class = ChapitreSerializer

    def get_queryset(self):
        theme_id = self.kwargs['theme_id']
        return Chapitre.objects.filter(theme_id=theme_id)

class AudioListView(generics.ListAPIView):
    serializer_class = AudioSerializer
    filterset_class = AudioFilter

    def get_queryset(self):
        queryset = Audio.objects.all()
        chapitre_id = self.request.query_params.get('chapitre')
        auteur_id = self.request.query_params.get('auteur')
        theme = self.request.query_params.get('theme')

        if chapitre_id:
            queryset = queryset.filter(chapitre_id=chapitre_id)
        if auteur_id:
            queryset = queryset.filter(auteur_id=auteur_id)
        if theme:
            # Filtrer via la relation indirecte: audio -> chapitre -> theme
            queryset = queryset.filter(chapitre__theme__nom_theme=theme)

        # Trier par date_audio (champ valide)
        return queryset.order_by('date_audio')