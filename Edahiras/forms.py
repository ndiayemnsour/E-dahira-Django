from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Membres

#Creation d'un formulaire personnalisé pour l’admin.
class MembresChangeForm(UserChangeForm):
    class Meta:
        model = Membres
        fields = '__all__'


class MembresCreationForm(UserCreationForm):
    class Meta:
        model = Membres
        fields = (
            "username", "email", "first_name", "last_name",
            "telephone", "photo", "role", "biography", "dahira",
        )
