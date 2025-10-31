# Fatigomètre - Application Web

Une application web interactive pour évaluer votre niveau de fatigue et obtenir une recommandation de produit à base de gelée royale Gelphore.

## Fonctionnalités

- **Réglette interactive** : Faites glisser le curseur pour sélectionner votre niveau de fatigue
- **5 niveaux de fatigue** :
  - Fatigue chez l'enfant
  - Fatigue légère
  - Fatigue modérée
  - Fatigue intense
  - Fatigue sévère
- **Animation de chargement** : Animation avec abeille et gelée royale pendant l'analyse
- **Recommandation personnalisée** : Affichage du produit recommandé selon votre niveau
- **Lien direct** : Bouton pour commander sur le site des Laboratoires Biotech

## Installation et Déploiement avec Docker

### Prérequis
- Docker installé sur votre système
- Docker Compose (optionnel, mais recommandé)

### Utilisation avec Docker Compose (Recommandé)

1. Construire et lancer l'application :
```bash
docker-compose up -d --build
```

2. L'application sera accessible à : `http://localhost:5000`

3. Arrêter l'application :
```bash
docker-compose down
```

### Utilisation avec Docker uniquement

1. Construire l'image :
```bash
docker build -t fatigometre .
```

2. Lancer le conteneur :
```bash
docker run -d -p 5000:5000 --name fatigometre-app fatigometre
```

3. L'application sera accessible à : `http://localhost:5000`

4. Arrêter le conteneur :
```bash
docker stop fatigometre-app
docker rm fatigometre-app
```

## Installation Locale (Sans Docker)

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

2. Lancer l'application :
```bash
python app.py
```

3. Ouvrir votre navigateur à l'adresse : `http://localhost:5000`

## Structure du projet

```
Fatigomère/
├── app.py                  # Application Flask principale
├── requirements.txt        # Dépendances Python
├── Dockerfile             # Configuration Docker
├── docker-compose.yml     # Configuration Docker Compose
├── .dockerignore          # Fichiers exclus du build Docker
├── static/
│   ├── style.css          # Styles CSS avec thème gelée royale
│   └── images/            # Images de l'application
├── templates/
│   ├── base.html          # Template de base
│   └── index.html         # Page principale avec réglette
└── README.md              # Documentation
```

## Technologies utilisées

- **Flask** : Framework web Python
- **Bootstrap 5** : Framework CSS
- **Bootstrap Icons** : Icônes
- **JavaScript** : Interactivité et animations
- **Docker** : Conteneurisation

## Design

L'interface utilise un thème aux couleurs de la gelée royale :
- Dégradés dorés et jaunes (#ffb300, #f57f17)
- Fond clair et chaleureux avec animations modernes
- Animations fluides et modernes
- Design responsive pour tous les appareils

## Notes

- L'application fonctionne en mode production dans Docker
- Le port par défaut est 5000
- Pour la production, envisagez d'utiliser un serveur WSGI comme Gunicorn

## Auteur

Développé pour les Laboratoires Biotech - Gelphore
