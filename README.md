# pipOSINT

Ceci est le dépôt Gitlab de notre projet de BSI : PIPOSINT, conduit durant l'année 2023-2024.
Le projet est dirigé par :

- Dorian Biojout
- Mathys Verglas
- Nicolas Le Tertre

## Arborescence


- `backend` : Code du backend.
  - `run.py` : Fonction principale du backend. 
  - `app` : Répertoire de l'API.
    - `models` : Structures des objets en sortie. (requêtes à la BDD interne)
    - `routes` : Routes de l'API.
    - `services` : Fonctions spécifiques aux routes.
    - `utils` : Fonctions générales.
  - `tests` : Tests des routes.
- `frontend` : Code du frontend.
- `docs` : Documentations du projet.