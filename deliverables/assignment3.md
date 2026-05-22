# Assignment 3 - Description et Comparaison des 3 Modèles

## 1. Baseline Model (Moving Average)
- **Principe** : prédit les points du joueur comme la moyenne de ses 5 derniers matchs (`AVG_PTS`).
- **Code** :

y_pred_baseline = X_test['AVG_PTS'].values 

- **Avantages** : extrêmement simple, pas d’entraînement, interprétable.

- **Inconvénients** : ne capture ni l’effet de l’adversaire, ni la fatigue, ni les tendances non linéaires.

## 2. XGBoost Regressor
- **Algorithme** : Gradient Boosting optimisé pour les données tabulaires.

- **Paramètres par défaut** : n_estimators=100, max_depth=6, learning_rate=0.3.

- **Points forts** : Gère les interactions complexes entre features. Robuste aux valeurs manquantes Permet d’obtenir l’importance des variables.

- **Performance** : MAE = 4.75, R² = 0.526

## 3. Random Forest (Optuna Optimized)
- **Algorithme** : Forêt d’arbres aléatoires avec bootstrap (bagging).

- **Optimisation** : recherche bayésienne via Optuna sur les hyperparamètres :

- n_estimators (100 – 500)
- max_depth (5 – 20)
- min_samples_split (2 – 10)
- min_samples_leaf (1 – 5)

- **Performance** : MAE = 4.82, R² = 0.514

## 4. Tableau comparatif des métriques

Modèle	MAE	R²	RMSE
Baseline (Moving Average)	4.95	0.484	6.36
XGBoost Regressor	        4.75	0.526	6.10
Random Forest (Optuna)	    4.82	0.514	6.18

## 5. Analyse et conclusion
XGBoost est le modèle retenu pour l’application Streamlit car il offre la MAE la plus basse et le R² le plus élevé.

Le Baseline sert de référence minimale acceptable.

Le Random Forest optimisé reste compétitif, mais légèrement moins performant sur ce jeu de données.

## 6. Fichiers des modèles (dossier models/)

model_baseline.pkl
model_xgboost.pkl
model_optuna.pkl
encoder.pkl
scaler.pkl
pca.pkl (optionnel)

## 7. Scripts d’entraînement (dossier scripts/)

train_baseline.py
train_xgboost.py
train_optuna.py