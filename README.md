# Exemple avec Django, Tailwindcss 4 et Swiper.js

## Installer les dépendances et tester

Cet exemple utiliser uv pour gérer les dépendances. N'hésitez pas à l'installer
en utilisant cette section de la [documentation](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

Ensuite, appliquez la procédure suivante

1. Installer les dépendances avec la commande `uv sync --dev`
2. A la racine du projet, Exécuter `uv run python manage.py migrate`, puis `uv run python manage.py runserver`
3. Dans frontend/, exécuter `npm install` puis `npm start`
4. Visiter la [page d'accueil du site](http://localhost:8000)