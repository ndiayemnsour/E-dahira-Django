import os
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
from rest_framework import viewsets
from .models import Membres, Audio, Sections, Localites, Dahiras, Sequence, Chapitre, Theme
from .serializers import MembresSerializer, DahirasSerializer, AudioSerializer, SectionsSerializer, LocalitesSerializer, \
    SequenceSerializer, ChapitreSerializer, ThemeSerializer
from django.http import FileResponse, Http404

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


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all().order_by('-date_audio')
    serializer_class = AudioSerializer
    #permission_classes = [IsAuthenticated]


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.all()
    serializer_class = SectionsSerializer
    #permission_classes = [IsAuthenticated]

class LocalitesViewSet(viewsets.ModelViewSet):
    queryset = Localites.objects.all()
    serializer_class = LocalitesSerializer
    #permission_classes = [IsAuthenticated]





