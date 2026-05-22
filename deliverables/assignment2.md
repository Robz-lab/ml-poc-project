# Assignment 2 - Feature Engineering et Dataset Préprocessé

## 1. Données brutes
- API NBA, saisons 2022-23 à 2025-26 (Regular Season + Playoffs)
- Chaque ligne : statistiques d’un joueur sur un match (PTS, MIN, FGA, FG3A, FTA, REB, AST, STL, BLK, TOV, PF, PLUS_MINUS, etc.)

## 2. Nettoyage initial
- Conversion de `GAME_DATE` en datetime
- Tri chronologique par `PLAYER_ID` et `GAME_DATE`
- Filtrage : `AVG_MIN >= 10` et `AVG_PTS > 2` (joueurs significatifs)

## 3. Création des features

### 3.1 Moyennes mobiles (5 matchs) – `AVG_*`
```python

for stat in ['PTS','MIN','FGA','FG3A','FTA','REB','AST','STL','BLK','TOV','PF','PLUS_MINUS']:
    df[f'AVG_{stat}'] = df.groupby('PLAYER_ID')[stat].transform(
        lambda x: x.rolling(5, min_periods=1).mean().shift(1)
    )

### 3.2 Forme récente (3 matchs) – SHORT_FORM_PTS

df['SHORT_FORM_PTS'] = df.groupby('PLAYER_ID')['PTS'].transform(
    lambda x: x.rolling(3, min_periods=1).mean().shift(1)
)

### 3.3 Fatigue et repos

df['DAYS_REST'] = df.groupby('PLAYER_ID')['GAME_DATE'].diff().dt.days.fillna(4)
df['IS_B2B'] = (df['DAYS_REST'] <= 1).astype(int)
df['RETURNING_FROM_ABSENCE'] = (df['DAYS_REST'] > 7).astype(int)

### 3.4 Titulaire

df['IS_STARTER'] = (df['AVG_MIN'] >= 25).astype(int)

### 3.5 Contexte du match

df['OPPONENT'] = df['MATCHUP'].apply(lambda x: str(x).split(' ')[-1] if pd.notna(x) else "UNK")
df['LOCATION'] = df['MATCHUP'].apply(lambda x: 'Away' if '@' in str(x) else 'Home')
df['DAY_OF_WEEK'] = df['GAME_DATE'].dt.day_name()

### 3.6 Force défensive adverse (Target encoding)

def_stats = df.groupby(['TEAM_ABBREVIATION','SEASON_YEAR'])['PTS'].mean().reset_index()
def_stats.columns = ['OPPONENT','SEASON_YEAR','OPP_AVG_PTS_ALLOWED']
df = df.merge(def_stats, on=['OPPONENT','SEASON_YEAR'], how='left')
df['OPP_AVG_PTS_ALLOWED'] = df['OPP_AVG_PTS_ALLOWED'].fillna(112.0) 

### 4. Features finales (22 colonnes)

AVG_PTS, SHORT_FORM_PTS, AVG_MIN, AVG_FGA, AVG_FG3A, AVG_FTA,
AVG_REB, AVG_AST, AVG_STL, AVG_BLK, AVG_TOV, AVG_PF,
AVG_PLUS_MINUS, DAYS_REST, IS_B2B, RETURNING_FROM_ABSENCE,
IS_STARTER, OPP_AVG_PTS_ALLOWED, TEAM_ABBREVIATION, OPPONENT,
LOCATION, DAY_OF_WEEK

### 5. Préprocessing avancé (src/features.py)
TableVectorizer (skrub) : target encoding des catégories + encodage cyclique des dates

StandardScaler : normalisation

PCA optionnelle (non utilisée par défaut) --> problème avec les modèles qui nobtenaient pas le meme nombre de features. 
