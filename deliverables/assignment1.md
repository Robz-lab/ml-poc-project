# Assignment 1 - NBA Points Prediction

**Nom du dataset :** NBA League Game Logs (Saisons 2020-2025)
**Source :** API officielle NBA via la librairie `nba_api`
**Lien :** https://github.com/swar/nba_api
**Type de données :** Données tabulaires structurées (statistiques de matchs)

**Variable cible (Target) :** `PTS` (Points marqués par match)

**Features principales :** - Minutes jouées (MIN)
- Adresse au tir (FG_PCT, FG3_PCT)
- Volume de tir (FGA, FG3A)
- Passes et rebonds (AST, REB)
- Impact global (PLUS_MINUS)

**Qualité des données :**
- **Valeurs manquantes :** 0% (nettoyage effectué lors de l'import)
- **Outliers :** Identifiés via boxplot (scores > 50-60 points), conservés car ils représentent des performances réelles d'élite.
- **Volume :** Environ XXXXX lignes (inscris ici le nombre exact que tu as eu).

**Limites éventuelles :**
Le dataset ne prend pas en compte l'état de fatigue (back-to-back) ou les blessures en cours de match qui peuvent fausser les prédictions.