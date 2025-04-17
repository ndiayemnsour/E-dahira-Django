# E-dahira 

Plateforme de gestion d'une Dahira (association religieuse), construite avec Django.

## Fonctionnalités
- Gestion des membres
- Enrigistrement audios 
- Historique des activités

## Installation

```bash
git clone https://github.com/ndiayemnsour/E-dahira-Django.git
cd E-dahira-Django
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sur Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
