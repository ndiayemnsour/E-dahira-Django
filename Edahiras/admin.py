from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Membres, Dahiras, Audio, Localites, Sections

@admin.register(Membres)
class MembresAdmin(UserAdmin):
    model = Membres
    fieldsets = UserAdmin.fieldsets + (
        ("Informations personnelles", {
            "fields": ["telephone", "photo", "dateInscription", "role", "biography", "dahira"]
        }),
    )

admin.site.register(Dahiras)
admin.site.register(Audio)
admin.site.register(Localites)
admin.site.register(Sections)



