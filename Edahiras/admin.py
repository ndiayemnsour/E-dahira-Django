from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .forms import MembresChangeForm, MembresCreationForm
from .models import Membres, Dahiras, Audio, Localites, Sections

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

    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'dahira', 'image_preview')

    def image_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.photo.url)
        return "Aucune photo"

    image_preview.short_description = "Aperçu de la photo"

admin.site.register(Dahiras)
admin.site.register(Audio)
admin.site.register(Localites)
admin.site.register(Sections)



