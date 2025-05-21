from rest_framework import serializers
from .models import Membres, Dahiras, Audio, Localites, Sections

#le serializer sert à convertir le modele en JSON
class DahirasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dahiras
        fields = "__all__"
        read_only_fields = ("id", "date_creation")

class MembresSerializer(serializers.ModelSerializer):
    dahira =DahirasSerializer( read_only=True)
    class Meta:
        model = Membres
        fields = ('email', 'first_name', 'last_name', 'telephone', 'role','photo', 'dahira' )
        read_only_fields = ("id", "date_creation")


class AudioSerializer(serializers.HyperlinkedModelSerializer):
    auteur = MembresSerializer(read_only=True)
    class Meta:
        model = Audio
        fields = "__all__"
        read_only_fields = ("id", "date_audio")

class LocalitesSerializer(serializers.ModelSerializer):
    dahira = DahirasSerializer(many=True, read_only=True)
    class Meta:
        model = Localites
        fields = "__all__"
        read_only_fields = ("id")

class SectionsSerializer(serializers.ModelSerializer):
    localites = LocalitesSerializer(many=True, read_only=True)
    class Meta:
        model = Sections
        fields = "__all__"
        read_only_fields = ("id")