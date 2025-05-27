from rest_framework import serializers
from .models import Membres, Dahiras, Audio, Localites, Sections, Theme, Chapitre, Sequence


#le serializer sert à convertir le modele en JSON
class DahirasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dahiras
        fields = "__all__"

class MembresSerializer(serializers.ModelSerializer):
    dahira =DahirasSerializer( read_only=True)
    class Meta:
        model = Membres
        fields = ('email', 'first_name', 'last_name', 'telephone', 'role','photo', 'dahira' )


class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = "__all__"

class ChapitreSerializer(serializers.ModelSerializer):
    sequence = SequenceSerializer(read_only=True)
    class Meta:
        model = Chapitre
        fields = "__all__"


class ThemeSerializer(serializers.ModelSerializer):
    chapitre = ChapitreSerializer(read_only=True)
    class Meta:
        model = Theme
        fields = "__all__"


class AudioSerializer(serializers.HyperlinkedModelSerializer):
    theme = ThemeSerializer(read_only=True)
    chapitre = ChapitreSerializer(read_only=True)
    sequence = SequenceSerializer(read_only=True)
    auteur = MembresSerializer(read_only=True)
    class Meta:
        model = Audio
        fields = "__all__"

class LocalitesSerializer(serializers.ModelSerializer):
    dahira = DahirasSerializer( read_only=True)
    class Meta:
        model = Localites
        fields = "__all__"

class SectionsSerializer(serializers.ModelSerializer):
    localites = LocalitesSerializer(many=True, read_only=True)
    class Meta:
        model = Sections
        fields = "__all__"
