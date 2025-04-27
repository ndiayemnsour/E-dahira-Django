from rest_framework import serializers
from .models import Membres, Dahiras, Audio, Localites, Sections

#le serializer sert à convertir le modele en JSON
class MembresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membres
        fields = "__all__"
        read_only_fields = ("id", "date_inscription")

class DahirasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dahiras
        fields = "__all__"
        read_only_fields = ("id", "date_creation")

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"
        read_only_fields = ("id", "date_audio")

class LocalitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localites
        fields = "__all__"
        read_only_fields = ("id")

class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = "__all__"
        read_only_fields = ("id")