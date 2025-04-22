from django.contrib.auth.models import AbstractUser
from django.db import models

# Les models E-dahira

#Classe dahira
class Dahiras(models.Model):
    nomDahira = models.CharField(max_length=200),
    siege = models.CharField(max_length=200),
    logo = models.ImageField(upload_to='media/image/'),
    dateCreation = models.DateField(auto_now=True),
    description = models.CharField(max_length=200),

    def __str__(self):
        return f"{self.nomDahira} {self.siege} {self.logo} {self.dateCreation} {self.description}"

#Classe Membres
class Membres(AbstractUser):
    biography = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=100),
    photo = models.ImageField(upload_to='media/image/'),
    dateInscription = models.DateField(auto_now=True),
    ROLE_CHOICES = [
        ('auditeur', 'Auditeur'),
        ('admin', 'Administrateur'),
        ('conferencier', 'Conferencier'),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='auditeur')
    dahira = models.ForeignKey(Dahiras, on_delete=models.CASCADE, related_name='membres', null=True, blank=True)

    def __str__(self):
        return f"{self.username} {self.biography} {self.role} {self.dahira.nomDahira if self.dahira else 'Aucun dahira'} {self.telephone}  {self.photo}  {self.dateInscription} {self.email} {self.password} {self.first_name} {self.last_name}"



# Classe Audio
class Audio(models.Model):
    theme = models.CharField(max_length=200),
    chapitre = models.CharField(max_length=200),
    sequence = models.CharField(max_length=200),
    audioFile = models.FileField(upload_to='media/audio/'),
    imageAudio = models.ImageField(upload_to='media/image/'),
    dateAudio = models.DateField(auto_now=True),
    duree = models.PositiveIntegerField(default=0),
    auteur = models.ForeignKey(Membres, on_delete=models.CASCADE, related_name='audio')

    def __str__(self):
        return f"{self.theme} {self.chapitre} {self.sequence} {self.audioFile} {self.imageAudio} {self.dateAudio} {self.duree} {self.auteur} "




#class localite
class Localites(models.Model):
    nomLocalite = models.CharField(max_length=200),
    dahira = models.ForeignKey(Dahiras, on_delete=models.CASCADE, related_name='localites')

    def __str__(self):
        return f"{self.nomLocalite} {self.dahira} "

#section
class Sections(models.Model):
    nomSection = models.CharField(max_length=200),
    localite = models.ForeignKey(Localites, on_delete=models.CASCADE, related_name='sections')

    def __str__(self):
        return f"{self.nomSection} {self.localite} "


