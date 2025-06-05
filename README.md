# E-dahira

Plateforme de gestion d'une Dahira (association religieuse), construite avec Django et Django REST Framework. E-dahira permet de gérer les membres, les contenus audio, et l'organisation hiérarchique des enseignements religieux.

## Table des matières
- [Présentation du projet](#présentation-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Architecture technique](#architecture-technique)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [API REST](#api-rest)
- [Structure du projet](#structure-du-projet)
- [Modèles de données](#modèles-de-données)

## Présentation du projet

E-dahira est une application web conçue pour faciliter la gestion des associations religieuses (Dahiras). Elle permet de centraliser les informations sur les membres, d'organiser et de diffuser des enseignements audio, et de structurer le contenu éducatif selon une hiérarchie thématique.

Le projet répond aux besoins des communautés religieuses souhaitant:
- Gérer efficacement leurs membres et leur organisation interne
- Diffuser des enseignements audio de manière structurée
- Organiser le contenu selon une hiérarchie thématique (thèmes, chapitres, séquences)
- Accéder aux contenus via une API REST pour des applications mobiles ou web

## Fonctionnalités

### Gestion des membres
- Inscription et authentification des utilisateurs
- Profils utilisateurs avec rôles différenciés (auditeur, administrateur, conférencier)
- Association des membres à des dahiras spécifiques

### Gestion des contenus audio
- Téléchargement et stockage de fichiers audio
- Validation automatique des formats et tailles de fichiers
- Organisation hiérarchique des contenus (thèmes, chapitres, séquences)
- Optimisation automatique des images associées

### Organisation structurelle
- Gestion des dahiras (associations religieuses)
- Organisation géographique (localités, sections)
- Hiérarchisation des enseignements (thèmes, chapitres, séquences)

### API REST
- Endpoints complets pour toutes les ressources
- Authentification JWT
- Filtrage et pagination des résultats
- Documentation des endpoints

## Architecture technique

### Technologies utilisées
- **Backend**: Django 5.2, Django REST Framework
- **Base de données**: SQLite (développement), compatible avec PostgreSQL (production)
- **Authentification**: JWT (JSON Web Tokens)
- **Gestion des médias**: Pillow pour l'optimisation des images
- **Sécurité**: Validation des fichiers, protection CSRF, authentification

### Composants principaux
- **Models**: Définition des entités et relations
- **Views**: API REST avec ViewSets et vues génériques
- **Serializers**: Conversion des modèles en JSON
- **Utils**: Fonctions utilitaires pour la validation et l'optimisation des fichiers
- **URLs**: Routage des requêtes API

## Installation

```bash
# Cloner le dépôt
git clone https://github.com/ndiayemnsour/E-dahira-Django.git
cd E-dahira-Django

# Créer et activer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement (voir section Configuration)

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur (administrateur)
python manage.py createsuperuser

# Lancer le serveur de développement
python manage.py runserver
```

## Configuration

Le projet utilise python-decouple pour gérer les variables d'environnement. Créez un fichier `.env` à la racine du projet avec les variables suivantes:

```
SECRET_KEY=votre_clé_secrète
DEBUG=True
DATABASE_URL=sqlite:///edahira.sqlite3
```

Pour la production, modifiez ces valeurs en conséquence:

```
SECRET_KEY=votre_clé_secrète_sécurisée
DEBUG=False
DATABASE_URL=postgres://user:password@localhost:5432/edahira
```

## Utilisation

### Interface d'administration

Accédez à l'interface d'administration Django à l'adresse `http://localhost:8000/admin/` et connectez-vous avec les identifiants du superutilisateur créé précédemment.

L'interface d'administration permet de:
- Gérer les utilisateurs et leurs rôles
- Créer et modifier des dahiras
- Gérer les thèmes, chapitres et séquences
- Télécharger et organiser les fichiers audio

### API REST

L'API REST est accessible à l'adresse `http://localhost:8000/api/`. Voir la section [API REST](#api-rest) pour plus de détails.

## API REST

L'API REST fournit des endpoints pour toutes les ressources du système:

### Authentification
- `POST /api/token/`: Obtenir un token JWT
- `POST /api/token/refresh/`: Rafraîchir un token JWT

### Ressources principales
- `GET /api/membres/`: Liste des membres
- `GET /api/dahiras/`: Liste des dahiras
- `GET /api/audios/`: Liste des fichiers audio
- `GET /api/themes/`: Liste des thèmes
- `GET /api/chapitres/`: Liste des chapitres
- `GET /api/sequences/`: Liste des séquences
- `GET /api/localites/`: Liste des localités
- `GET /api/sections/`: Liste des sections

### Endpoints spécifiques
- `GET /api/themes/{id}/chapitres/`: Chapitres d'un thème spécifique
- `GET /audios/`: Liste filtrée des fichiers audio

Chaque endpoint supporte les opérations CRUD standard (GET, POST, PUT, DELETE) avec les permissions appropriées.

## Structure du projet

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

## Modèles de données

### Dahiras
Représente une association religieuse avec:
- Nom, siège, logo, date de création, description

### Membres
Utilisateurs du système avec:
- Informations personnelles (nom, prénom, email, téléphone)
- Rôle (auditeur, administrateur, conférencier)
- Association à un dahira

### Organisation du contenu
- **Theme**: Catégorie principale des enseignements
- **Chapitre**: Subdivision d'un thème
- **Sequence**: Subdivision d'un chapitre

### Audio
Fichiers audio avec:
- Fichier audio, image associée, date
- Relations avec auteur, thème, chapitre, séquence

### Organisation géographique
- **Localites**: Zones géographiques associées à un dahira
- **Sections**: Subdivisions d'une localité
