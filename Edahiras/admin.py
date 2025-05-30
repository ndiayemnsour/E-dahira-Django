from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .forms import MembresChangeForm, MembresCreationForm
from .models import Membres, Dahiras, Audio, Localites, Sections, Theme, Chapitre, Sequence

admin.site.register(Theme)
admin.site.register(Chapitre)
admin.site.register(Sequence)

@admin.register(Membres)
class MembresAdmin(UserAdmin):
    form = MembresChangeForm
    add_form = MembresCreationForm
    model = Membres
    readonly_fields = ['date_inscription']

    fieldsets = (
        ("Identifiants", {
            "fields": ("username", "password")
        }),
        ("Informations personnelles", {
            "fields": ("first_name", "last_name", "email", "telephone", "photo", "role", "biography", "dahira",
                       "date_inscription")
        }),
        ("Permissions", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions"),
        }),
        ("Dates importantes", {
            "fields": ("last_login", "date_joined"),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "first_name", "last_name", "telephone", "photo",
                       "role", "biography", "dahira"),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'nom_dahira', 'image_preview')

    # Pour affichier l'image
    def image_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.photo.url)
        return "Aucune photo"

    image_preview.short_description = "Aperçu de la photo"

    #Pour afficher juste le nom dahira pas L'objet dahira
    def nom_dahira(self, obj):
        return obj.dahira.nom_dahira if obj.dahira else "Aucun"

    nom_dahira.short_description = "Dahira"

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = (
        #'theme',
        'chapitre',
        'sequence',
        'audio_file',
        'image_audio',
        'date_audio',
        'nom_auteur',
        'play_audio',
    )

    #Pour affichier l'audio en mode lecture
    def play_audio(self, obj):
        return format_html('<audio controls><source src="{}" type="audio/mpeg"></audio>', obj.audio_file.url)

    play_audio.short_description = "Lecture"

    #Pour afficher le nom de L'auteur uniquement au lieu de retourner tout l'objet
    def nom_auteur(self, obj):
        return obj.auteur.first_name+" "+obj.auteur.last_name if obj.auteur else "Anonyme"

    nom_auteur.short_description = "Auteur"


@admin.register(Localites)
class LocalitesAdmin(admin.ModelAdmin):
    list_display = ('nom_localite', 'nom_dahira')

    # Pour afficher juste le nom dahira pas L'objet dahira
    def nom_dahira(self, obj):
        return obj.dahira.nom_dahira if obj.dahira else "Aucun"


@admin.register(Sections)
class SectionsAdmin(admin.ModelAdmin):
    list_display = ('nom_section', 'nom_localite')
    def nom_localite(self, obj):
        return obj.localite.nom_localite if obj.localite else "Anonyme"


@admin.register(Dahiras)
class DahirasAdmin(admin.ModelAdmin):
    readonly_fields = ['date_creation']
    list_display = ('nom_dahira', 'siege', 'logo', 'date_creation', 'description')





