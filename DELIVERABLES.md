# TP Machine Learning in Production - Livrables

## 📦 Repository GitHub
**URL** : `https://github.com/<TON-USERNAME>/<TON-REPO>`

---

## 📸 Screenshots Requis

### 1. Git Hook Local (pre-push)
**Commande exécutée** :
```bash
.git/hooks/pre-push
```

**Sortie attendue** :
```
Running ruff...
All checks passed!
Running tests...
======================================================= test session starts ========================================================
platform darwin -- Python 3.13.3, pytest-9.0.1, pluggy-1.6.0
rootdir: /Users/alondebasc/Downloads/Archive
configfile: pyproject.toml
collected 8 items

tests/test_integration_example.py ...                                                                                        [ 37%]
tests/test_unit_example.py .....                                                                                             [100%]

======================================================== 8 passed in 0.11s =========================================================
All checks passed. Proceeding with push.
```

📷 **À faire** : Prendre un screenshot de ton terminal avec cette sortie

---

### 2. GitHub Workflow CI

**Étapes pour obtenir le screenshot** :

1. **Créer le repo GitHub et pousser** :
   ```bash
   git remote add origin https://github.com/<ton-username>/<ton-repo>.git
   git branch -M main
   git push -u origin main
   ```

2. **Créer et pousser la branche dev** :
   ```bash
   git checkout -b dev
   git push -u origin dev
   ```

3. **Créer une Pull Request** :
   - Va sur GitHub : `https://github.com/<ton-username>/<ton-repo>`
   - Clique sur "Pull requests" → "New pull request"
   - Base: `dev` ← Compare: `main`
   - Crée la PR

4. **Attendre que le workflow s'exécute** :
   - Le workflow `.github/workflows/ci.yml` se déclenchera automatiquement
   - Va dans l'onglet "Actions" ou regarde les checks dans la PR

5. **Prendre le screenshot** montrant :
   - ✅ Le workflow "CI" avec status "passed"
   - ✅ Les étapes : Checkout code, Set up Python, Install dependencies, Run Ruff linting, Run tests
   - ✅ Tout en vert

📷 **À faire** : Screenshot de la page GitHub Actions ou de la PR avec les checks passés

---

## ✅ Checklist Finale

- [ ] Repo GitHub créé et code pushé
- [ ] Branche `dev` créée et pushée
- [ ] Screenshot du git hook local (terminal)
- [ ] Screenshot du workflow GitHub (navigateur)
- [ ] Lien du repo fourni

---

## 🎯 Fonctionnalités Implémentées

1. ✅ Environnement virtuel Python + dépendances
2. ✅ Configuration Ruff (linting)
3. ✅ Tests unitaires + intégration (8 tests)
4. ✅ Git hook pre-push (bloque si erreurs)
5. ✅ CI GitHub sur PRs vers `dev`

---

## 📝 Notes

- Le hook pre-push empêche de pousser du code avec des erreurs de linting ou des tests qui échouent
- La CI GitHub assure une double vérification sur chaque PR vers `dev`
- Tous les commits sont tracés avec des messages clairs
