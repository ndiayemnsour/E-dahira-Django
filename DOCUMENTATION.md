# Documentation Technique E-dahira

## Table des matières
- [Introduction](#introduction)
- [Architecture du projet](#architecture-du-projet)
- [Modèles de données](#modèles-de-données)
- [API REST](#api-rest)
- [Authentification et sécurité](#authentification-et-sécurité)
- [Gestion des fichiers médias](#gestion-des-fichiers-médias)
- [Configuration et déploiement](#configuration-et-déploiement)
- [Extension du projet](#extension-du-projet)
- [Bonnes pratiques](#bonnes-pratiques)

## Introduction

Cette documentation technique est destinée aux développeurs qui souhaitent comprendre, maintenir ou étendre le projet E-dahira. Elle fournit des informations détaillées sur l'architecture, les modèles de données, l'API REST et d'autres aspects techniques du projet.

## Architecture du projet

### Structure des répertoires

```
Edahira/
├── Edahira/              # Configuration du projet Django
│   ├── settings.py       # Paramètres du projet
│   ├── urls.py           # URLs racine
│   └── wsgi.py           # Configuration WSGI
├── Edahiras/             # Application principale
│   ├── admin.py          # Configuration de l'interface d'administration
│   ├── models.py         # Modèles de données
│   ├── serializers.py    # Sérialiseurs pour l'API REST
│   ├── urls.py           # URLs de l'application
│   ├── utils.py          # Fonctions utilitaires
│   └── views.py          # Vues et ViewSets
├── media/                # Fichiers média téléchargés
│   ├── audio/            # Fichiers audio
│   └── image/            # Images
├── .env                  # Variables d'environnement
├── manage.py             # Script de gestion Django
└── requirements.txt      # Dépendances du projet
```

### Composants principaux

1. **Configuration Django** (`Edahira/`): Contient les paramètres globaux du projet, les URLs racines et la configuration WSGI.

2. **Application principale** (`Edahiras/`): Contient tous les composants de l'application:
   - Modèles de données
   - Vues et ViewSets pour l'API
   - Sérialiseurs pour la conversion des données
   - URLs de l'application
   - Fonctions utilitaires

3. **Fichiers média** (`media/`): Stocke les fichiers téléchargés par les utilisateurs.

4. **Configuration d'environnement** (`.env`): Contient les variables d'environnement pour la configuration du projet.

### Flux de données

1. Les requêtes HTTP sont reçues par le serveur Django.
2. Les URLs sont routées vers les vues appropriées via les fichiers `urls.py`.
3. Les vues traitent les requêtes et interagissent avec les modèles.
4. Les données sont sérialisées en JSON pour les réponses API.
5. Les réponses sont renvoyées au client.

## Modèles de données

### Diagramme de relations

```
Dahiras <---> Membres <---> Audio
   |            |            |
   v            v            v
Localites     Chapitre <--- Theme
   |            |
   v            v
Sections     Sequence
```

### Description détaillée des modèles

#### Dahiras

```python
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
```

Le modèle `Dahiras` représente une association religieuse avec:
- Un nom
- Un siège (localisation)
- Un logo (image)
- Une date de création
- Une description

#### Membres

```python
class Membres(AbstractUser):
    biography = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
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
```

Le modèle `Membres` étend `AbstractUser` de Django et ajoute:
- Une biographie
- Un numéro de téléphone
- Une photo de profil
- Une date d'inscription
- Un rôle (auditeur, administrateur, conférencier)
- Une relation avec un Dahira

#### Organisation du contenu

```python
class Theme(models.Model):
    nom_theme = models.CharField(max_length=150)

class Chapitre(models.Model):
    nom_chapitre = models.CharField(max_length=150)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='chapitres', null=True, blank=True)
    auteur = models.ForeignKey(Membres, on_delete=models.CASCADE, related_name='chapitres', null=True, blank=True)

class Sequence(models.Model):
    nom_sequence = models.CharField(max_length=150)
    chapitre = models.ForeignKey('Chapitre', on_delete=models.CASCADE, related_name='sequences', null=True, blank=True)
```

Ces modèles forment une hiérarchie pour organiser le contenu:
- `Theme`: Catégorie principale
- `Chapitre`: Subdivision d'un thème, associé à un auteur
- `Sequence`: Subdivision d'un chapitre

#### Audio

```python
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
```

Le modèle `Audio` représente un fichier audio avec:
- Un nom
- Un fichier audio
- Une image associée
- Une date d'enregistrement
- Des relations avec l'auteur, le thème, le chapitre et la séquence

#### Organisation géographique

```python
class Localites(models.Model):
    nom_localite = models.CharField(max_length=200)
    dahira = models.ForeignKey(Dahiras, on_delete=models.CASCADE, related_name='localites')

class Sections(models.Model):
    nom_section = models.CharField(max_length=200)
    localite = models.ForeignKey(Localites, on_delete=models.CASCADE, related_name='sections')
```

Ces modèles représentent l'organisation géographique:
- `Localites`: Zones géographiques associées à un Dahira
- `Sections`: Subdivisions d'une localité

## API REST

### Configuration de l'API

L'API REST est configurée dans `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}
```

### ViewSets

Les ViewSets sont définis dans `views.py` et fournissent les opérations CRUD pour chaque modèle:

```python
class MembresViewSet(viewsets.ModelViewSet):
    queryset = Membres.objects.all()
    serializer_class = MembresSerializer

class DahirasViewSet(viewsets.ModelViewSet):
    queryset = Dahiras.objects.all()
    serializer_class = DahirasSerializer

# Autres ViewSets...
```

### Sérialiseurs

Les sérialiseurs sont définis dans `serializers.py` et convertissent les modèles en JSON:

```python
class DahirasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dahiras
        fields = "__all__"

class MembresSerializer(serializers.ModelSerializer):
    dahira = DahirasSerializer(read_only=True)
    class Meta:
        model = Membres
        fields = ('email', 'first_name', 'last_name', 'telephone', 'role', 'photo', 'dahira')

# Autres sérialiseurs...
```

### Endpoints

Les endpoints sont définis dans `urls.py`:

```python
router = routers.DefaultRouter()
router.register(r'membres', MembresViewSet)
router.register(r'dahiras', DahirasViewSet)
router.register(r'audios', AudioViewSet)
router.register(r'localites', LocalitesViewSet)
router.register(r'sections', SectionsViewSet)
router.register(r'chapitres', ChapitreViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'sequences', SequenceViewSet)

urlpatterns = [
    path('audios/', AudioListView.as_view(), name='audio-list'),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/themes/<int:theme_id>/chapitres/', ChapitresByThemeAPIView.as_view(), name='chapitres-by-theme'),
    # Autres URLs...
]
```

### Filtrage et pagination

L'API supporte le filtrage et la pagination:

```python
class AudioListView(generics.ListAPIView):
    serializer_class = AudioSerializer
    filterset_class = AudioFilter

    def get_queryset(self):
        queryset = Audio.objects.all()
        chapitre_id = self.request.query_params.get('chapitre')
        auteur_id = self.request.query_params.get('auteur')
        theme = self.request.query_params.get('theme')

        if chapitre_id:
            queryset = queryset.filter(chapitre_id=chapitre_id)
        if auteur_id:
            queryset = queryset.filter(auteur_id=auteur_id)
        if theme:
            queryset = queryset.filter(chapitre__theme__nom_theme=theme)

        return queryset.order_by('date_audio')
```

## Authentification et sécurité

### JWT (JSON Web Tokens)

L'authentification utilise JWT via `rest_framework_simplejwt`:

```python
# Dans urls.py
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
```

### Permissions

Les permissions sont définies dans les ViewSets:

```python
class MembresViewSet(viewsets.ModelViewSet):
    queryset = Membres.objects.all()
    serializer_class = MembresSerializer
    # permission_classes = [IsAuthenticated]  # Commenté mais peut être activé
```

### Validation des fichiers

Les fichiers téléchargés sont validés dans `utils.py`:

```python
def validate_image_file(file):
    # Vérifier l'extension du fichier
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            _('Format de fichier non supporté. Les formats autorisés sont: %(extensions)s'),
            params={'extensions': ', '.join(ALLOWED_IMAGE_EXTENSIONS)},
        )
    
    # Vérifier le type MIME
    if hasattr(file, 'content_type') and file.content_type not in ALLOWED_IMAGE_CONTENT_TYPES:
        raise ValidationError(
            _('Type de contenu non supporté. Les types autorisés sont: %(types)s'),
            params={'types': ', '.join(ALLOWED_IMAGE_CONTENT_TYPES)},
        )
    
    # Vérifier la taille du fichier
    if file.size > IMAGE_MAX_SIZE_MB * 1024 * 1024:
        raise ValidationError(
            _('La taille du fichier ne doit pas dépasser %(size)s MB'),
            params={'size': IMAGE_MAX_SIZE_MB},
        )
```

## Gestion des fichiers médias

### Configuration

Les fichiers médias sont configurés dans `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Optimisation des images

Les images sont optimisées dans `utils.py`:

```python
def optimize_image(image_field):
    # Ouvrir l'image avec Pillow
    img = Image.open(image_field)
    
    # Conserver le format d'origine
    if img.format not in ['JPEG', 'PNG']:
        img_format = 'JPEG'  # Format par défaut
    else:
        img_format = img.format
    
    # Convertir en RGB si nécessaire
    if img.mode != 'RGB' and img_format == 'JPEG':
        img = img.convert('RGB')
    
    # Redimensionner l'image si elle dépasse les dimensions maximales
    if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
        img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
    
    # Créer un buffer pour stocker l'image optimisée
    output = io.BytesIO()
    
    # Enregistrer l'image avec compression
    if img_format == 'JPEG':
        img.save(output, format='JPEG', quality=85, optimize=True)
    else:  # PNG
        img.save(output, format='PNG', optimize=True)
    
    # Réinitialiser le pointeur du buffer
    output.seek(0)
    
    # Créer un nouvel objet de fichier à partir du buffer
    return InMemoryUploadedFile(
        output,
        'ImageField',
        f"{os.path.splitext(image_field.name)[0]}.{img_format.lower()}",
        f'image/{img_format.lower()}',
        output.getbuffer().nbytes,
        None
    )
```

### Servir les fichiers audio

Les fichiers audio sont servis avec un content-type approprié:

```python
def serve_audio_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'audio', filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='audio/mpeg')
    else:
        raise Http404("Fichier audio non trouvé")
```

## Configuration et déploiement

### Variables d'environnement

Le projet utilise `python-decouple` pour gérer les variables d'environnement:

```python
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

### Base de données

La configuration de la base de données utilise `dj_database_url`:

```python
DATABASES = {
    'default': dj_database_url.parse(
        config('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "edahira.sqlite3"}')
    )
}
```

### Serveur WSGI

Le projet est configuré pour utiliser WSGI:

```python
WSGI_APPLICATION = "Edahira.wsgi.application"
```

### Fichiers statiques

Les fichiers statiques sont configurés avec whitenoise:

```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## Extension du projet

### Ajout d'un nouveau modèle

Pour ajouter un nouveau modèle:

1. Définir le modèle dans `models.py`
2. Créer un sérialiseur dans `serializers.py`
3. Créer un ViewSet dans `views.py`
4. Enregistrer le ViewSet dans le routeur dans `urls.py`
5. Créer et appliquer les migrations

### Modification d'un modèle existant

Pour modifier un modèle existant:

1. Modifier la définition du modèle dans `models.py`
2. Mettre à jour le sérialiseur si nécessaire
3. Créer et appliquer les migrations

### Ajout d'un nouvel endpoint

Pour ajouter un nouvel endpoint:

1. Créer une nouvelle vue dans `views.py`
2. Ajouter l'URL dans `urls.py`

## Bonnes pratiques

### Validation des données

Toujours valider les données entrantes:

```python
def validate_audio_file(file):
    # Vérifier l'extension du fichier
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ALLOWED_AUDIO_EXTENSIONS:
        raise ValidationError(
            _('Format de fichier non supporté. Les formats autorisés sont: %(extensions)s'),
            params={'extensions': ', '.join(ALLOWED_AUDIO_EXTENSIONS)},
        )
    
    # Autres validations...
```

### Optimisation des performances

Optimiser les requêtes de base de données:

```python
# Utiliser select_related pour les relations ForeignKey
queryset = Audio.objects.select_related('chapitre', 'auteur').all()

# Utiliser prefetch_related pour les relations ManyToMany
queryset = Dahiras.objects.prefetch_related('membres').all()
```

### Sécurité

Suivre les bonnes pratiques de sécurité:

- Ne pas exposer de données sensibles dans les sérialiseurs
- Valider tous les fichiers téléchargés
- Utiliser des permissions appropriées pour chaque endpoint
- Activer HTTPS en production
- Ne pas stocker de secrets dans le code source