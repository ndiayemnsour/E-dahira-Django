import django_filters
from .models import Audio

class AudioFilter(django_filters.FilterSet):
    theme = django_filters.CharFilter(field_name='chapitre__theme__nom_theme', lookup_expr='icontains')
    auteur_first_name = django_filters.CharFilter(field_name='chapitre__auteur__first_name', lookup_expr='icontains')
    auteur_last_name = django_filters.CharFilter(field_name='chapitre__auteur__last_name', lookup_expr='icontains')

    class Meta:
        model = Audio
        fields = ['theme', 'auteur_first_name', 'auteur_last_name']