# E-dahira - Présentation du Projet

## Introduction

**E-dahira** est une plateforme de gestion d'associations religieuses (Dahiras) développée avec Django et Django REST Framework.

Cette présentation donne un aperçu du projet, de ses fonctionnalités, de son architecture technique et de ses cas d'utilisation.

---

## Qu'est-ce qu'une Dahira?

Une **Dahira** est une association religieuse, généralement dans le contexte des confréries musulmanes d'Afrique de l'Ouest, qui:
- Organise des enseignements religieux
- Rassemble des membres partageant des valeurs communes
- Diffuse des connaissances à travers des conférences et des enregistrements audio

---

## Problématique

Les Dahiras font face à plusieurs défis:
- Gestion manuelle des membres et des cotisations
- Difficulté à organiser et partager les enseignements audio
- Manque de structure pour les contenus éducatifs
- Absence de plateforme centralisée pour la communauté

---

## Solution: E-dahira

E-dahira répond à ces défis en offrant:
- Une plateforme centralisée pour la gestion des membres
- Un système d'organisation et de diffusion des enseignements audio
- Une structure hiérarchique pour les contenus éducatifs
- Une API REST pour l'intégration avec d'autres applications

---

## Fonctionnalités Principales

### Gestion des Membres
- Profils utilisateurs avec différents rôles
- Authentification sécurisée
- Association des membres à des Dahiras

### Gestion des Contenus Audio
- Organisation hiérarchique (Thèmes → Chapitres → Séquences)
- Téléchargement et validation des fichiers audio
- Optimisation automatique des images

### Organisation Structurelle
- Gestion des Dahiras, localités et sections
- Hiérarchisation des enseignements

---

## Architecture Technique

### Technologies Utilisées
- **Backend**: Django 5.2, Django REST Framework
- **Base de données**: SQLite/PostgreSQL
- **Authentification**: JWT (JSON Web Tokens)
- **Gestion des médias**: Pillow pour l'optimisation des images

### Architecture
- Architecture MVC (Model-View-Controller)
- API REST pour la communication avec les clients
- Système de permissions basé sur les rôles

---

## Modèles de Données

### Principaux Modèles
- **Dahiras**: Associations religieuses
- **Membres**: Utilisateurs du système (extension de AbstractUser)
- **Theme/Chapitre/Sequence**: Organisation hiérarchique du contenu
- **Audio**: Fichiers audio liés à la hiérarchie de contenu
- **Localites/Sections**: Organisation géographique

---

## API REST

L'application expose une API REST complète:
- Endpoints pour toutes les ressources
- Authentification JWT
- Filtrage et pagination
- Opérations CRUD avec permissions appropriées

---

## Sécurité

Le projet intègre plusieurs mesures de sécurité:
- Validation des fichiers uploadés (type, taille)
- Optimisation des images pour éviter les attaques
- Authentification JWT pour l'API
- Protection CSRF pour les formulaires
- Gestion des permissions basée sur les rôles

---

## Cas d'Utilisation

### Pour les Administrateurs de Dahiras
- Gestion centralisée des membres
- Organisation des contenus éducatifs
- Suivi des activités

### Pour les Conférenciers
- Partage facile des enseignements audio
- Organisation structurée du contenu
- Diffusion à un public plus large

### Pour les Auditeurs
- Accès aux enseignements de manière structurée
- Recherche et filtrage des contenus
- Suivi des nouveaux enseignements

---

## Avantages et Bénéfices

- **Centralisation**: Toutes les informations au même endroit
- **Structuration**: Organisation claire des contenus
- **Accessibilité**: Disponible via web et API pour applications mobiles
- **Évolutivité**: Architecture modulaire permettant l'ajout de fonctionnalités
- **Sécurité**: Protection des données et des contenus

---

## Perspectives d'Évolution

- Application mobile pour les membres
- Système de paiement pour les cotisations
- Fonctionnalités de streaming audio en direct
- Statistiques et analyses d'utilisation
- Intégration de fonctionnalités communautaires (forums, commentaires)

---

## Conclusion

E-dahira est une solution complète pour la gestion des associations religieuses, offrant:
- Une plateforme centralisée et structurée
- Des fonctionnalités adaptées aux besoins spécifiques des Dahiras
- Une architecture technique moderne et évolutive
- Une base solide pour de futures améliorations

---

## Contact et Ressources

- **GitHub**: [github.com/ndiayemnsour/E-dahira-Django](https://github.com/ndiayemnsour/E-dahira-Django)
- **Documentation**: Voir le fichier README.md du projet
- **Installation**: Instructions détaillées dans la documentation