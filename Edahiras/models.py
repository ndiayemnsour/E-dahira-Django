from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import validate_image_file, validate_audio_file, optimize_image

# --- Classe Dahira ---
class Dahiras(models.Model):
    nom_dahira = models.CharField(max_length=150)
    siege = models.CharField(max_length=200)
    logo = models.ImageField(
        upload_to='media/image/',
        validators=[validate_image_file],
        help_text="Image au format JPG, JPEG, PNG ou GIF (max. 15 MB)",
    )
    date_creation = models.DateField(auto_now=True)
    description = models.CharField(max_length=200, default="description")

    def save(self, *args, **kwargs):
        if self.logo and hasattr(self.logo, 'file'):
            self.logo = optimize_image(self.logo)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom_dahira}"

# --- Classe Membres (utilisateur) ---
class Membres(AbstractUser):
    biography = models.TextField(blank=True, null=True)
    telephone  = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(
        upload_to='media/image/',
        validators=[validate_image_file],
        help_text="Image au format JPG, JPEG, PNG ou GIF (max. 50 MB)",
        blank=True, null=True
    )
    date_inscription = models.DateField(auto_now=True)
    ROLE_CHOICES = [
        ('auditeur', 'Auditeur'),
        ('admin', 'Administrateur'),
        ('conferencier', 'Conferencier'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    dahira = models.ForeignKey(Dahiras, on_delete=models.CASCADE, related_name='membres', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.photo and hasattr(self.photo, 'file'):
            self.photo = optimize_image(self.photo)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# --- Classe Sequence ---
class Sequence(models.Model):
    nom_sequence = models.CharField(max_length=150)
    chapitre = models.ForeignKey('Chapitre', on_delete=models.CASCADE, related_name='sequences', null=True, blank=True)

    def __str__(self):
        return f"{self.nom_sequence}"

# --- Classe Theme ---
class Theme(models.Model):
    nom_theme = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nom_theme}"

# --- Classe Chapitre ---
class Chapitre(models.Model):
    nom_chapitre = models.CharField(max_length=150)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='chapitres', null=True, blank=True)
    auteur = models.ForeignKey(Membres, on_delete=models.CASCADE, related_name='chapitres', null=True, blank=True)  # <-- ajout

    def __str__(self):
        return f"{self.nom_chapitre}"


# --- Classe Audio ---
class Audio(models.Model):
    nom_audio = models.CharField(max_length=150, null=True, blank=True, default='Audio')
    audio_file = models.FileField(
        upload_to='media/audio/',
        validators=[validate_audio_file],
        help_text="Fichier audio au format MP3, WAV, OGG ou M4A (max. 20 MB)",
        null=True,
        blank=True
    )
    image_audio = models.ImageField(
        upload_to='media/image/',
        validators=[validate_image_file],
        help_text="Image au format JPG, JPEG, PNG ou GIF (max. 5 MB)",
    )
    date_audio = models.DateField(auto_now=True, null=True, blank=True)
    auteur = models.ForeignKey(Membres, on_delete=models.CASCADE, related_name='audio')
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='audio', null=True, blank=True)
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE, related_name='audio')
    sequence = models.ForeignKey(Sequence, on_delete=models.CASCADE, related_name='audio', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image_audio and hasattr(self.image_audio, 'file'):
            self.image_audio = optimize_image(self.image_audio)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.chapitre} {self.sequence}"

# --- Classe Localites ---
class Localites(models.Model):
    nom_localite = models.CharField(max_length=200)
    dahira = models.ForeignKey(Dahiras, on_delete=models.CASCADE, related_name='localites')

    def __str__(self):
        return f"{self.nom_localite}"

# --- Classe Sections ---
class Sections(models.Model):
    nom_section = models.CharField(max_length=200)
    localite = models.ForeignKey(Localites, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return f"{self.nom_section}"