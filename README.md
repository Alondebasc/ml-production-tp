# ML in Production - TP Setup

Ce projet implémente les bonnes pratiques MLOps pour un projet Flask.

## Setup Initial

```bash
# Créer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
pip install ruff pytest
```

## Installation du Git Hook

```bash
# Copier le hook pre-push
cp pre-push.sh .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

## Vérifications de Qualité

### Linting avec Ruff
```bash
ruff check app.py
```

### Tests avec Pytest
```bash
pytest -v
```

## Workflow

1. **Développement local** : Le hook pre-push vérifie automatiquement ruff + pytest avant chaque push
2. **Pull Requests vers `dev`** : La CI GitHub exécute les mêmes checks automatiquement
3. **Protection** : Impossible de merger si les checks échouent

## Structure du Projet

```
.
├── app.py                      # Application Flask
├── templates/                  # Templates HTML
├── static/                     # CSS/JS statiques
├── tests/                      # Tests unitaires et d'intégration
│   ├── test_unit_example.py
│   └── test_integration_example.py
├── .github/workflows/          # CI GitHub Actions
│   └── ci.yml
├── pyproject.toml              # Configuration Ruff
├── requirements.txt            # Dépendances Python
└── pre-push.sh                 # Script de hook Git
```

## Fonctionnalités Implémentées

- ✅ Environnement virtuel Python
- ✅ Configuration Ruff (linting)
- ✅ Tests unitaires et d'intégration (pytest)
- ✅ Git hook pre-push (bloque push si erreurs)
- ✅ CI GitHub sur PRs vers `dev`
