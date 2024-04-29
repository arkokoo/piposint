# pipOSINT

Ceci est le dépôt Gitlab de notre projet de BSI : PIPOSINT, conduit durant l'année 2023-2024.
Le projet est dirigé par :

- Dorian Biojout
- Mathys Verglas
- Nicolas Le Tertre

## Arborescence

- `docker-compose.yml` : Installe l'environnement complet de l'outil
- `backend/` : Code du backend
  - `.env` : Fichier d'inventaire (à configurer avant lancement des conteneurs)
  - `run.py` : Fonction principale du backend
  - `history/` : Dossier contenant les json des requêtes effectuées.
  - `app/` : Répertoire de l'API
    - `routes/` : Routes de l'API
    - `services/` : Fonctions spécifiques aux routes
    - `utils/` : Fonctions générales
    - `tests/` : Tests des routes
- `frontend/` : Code du frontend
- `overpass-turbo/` : Code du service overpass-turbo
  - `app/` : Patch d'intégration à la solution
- `docs/` : Documentations du projet

## Installation

Création des conteneurs :
```bash
sudo docker-compose up -d --build
```

## Le front

Ce frontend est développé Vue 3 et Vite.

Extension(s) recommandée(s) pour vscode :
- [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (désactivé Vetur si jamais)

Le dossier "screenshot" contient un aperçu rapide du site.

### Le setup

```sh
cd frontend
npm install
```

#### Compilation

```sh
npm run dev
```