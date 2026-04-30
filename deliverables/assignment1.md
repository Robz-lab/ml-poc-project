# Assignment 1 - NBA Points Prediction Project

## 1. Informations sur le Dataset
* **Nom du dataset :** NBA League Game Logs (Multi-Seasons)
* **Source :** API officielle de la NBA via la bibliothèque Python `nba_api`.
* **Lien :** [https://github.com/swar/nba_api](https://github.com/swar/nba_api)
* **Type de données :** Données tabulaires structurées (séries temporelles de statistiques de performance par match).

## 2. Définition du Problème ML
* **Variable cible (Target) :** `PTS` (Nombre de points marqués par un joueur lors d'un match).
* **Type de ML :** Apprentissage supervisé - **Régression**.
* **Features principales :** * `MIN` (Minutes jouées)
    * `FGA` / `FG_PCT` (Tentatives et adresse au tir)
    * `FG3A` / `FG3_PCT` (Tentatives et adresse à 3 points)
    * `AST` (Passes décisives)
    * `REB` (Rebonds)
    * `PLUS_MINUS` (Impact global sur le score)

## 3. Qualité des Données et Checks
* **Données manquantes :** * **0%** de valeurs manquantes. 
    * *Note :* Un nettoyage a été effectué directement via le script d'importation (`src/data.py`) pour supprimer les entrées incomplètes et filtrer les joueurs ayant joué moins de 5 minutes.
* **Détection des Outliers :** * Méthode utilisée : **Interquartile Range (IQR)**.
    * **Décision :** Les outliers ont été identifiés (notamment les performances à plus de 50 points) mais **conservés**. En NBA, ces données représentent des performances d'élite réelles et non des erreurs de mesure ; elles sont cruciales pour que le modèle apprenne les hauts scores.
* **Feature Drift & Distribution :** * Les distributions des variables comme `MIN` et `PTS` ont été vérifiées par histogrammes. Elles présentent une distribution normale décalée, cohérente avec la réalité du temps de jeu en ligue professionnelle.

## 4. Limites éventuelles
* Le dataset ne contient pas de données contextuelles externes comme l'état de fatigue (matchs joués deux jours de suite / back-to-back), les blessures mineures non signalées, ou l'avantage du terrain (Home/Away), ce qui pourrait limiter la précision absolue du modèle.