from nba_api.stats.endpoints import playercareerstats
from sklearn.model_selection import train_test_split


def load_dataset_split():
    player_id = "2544"  # LeBron James

    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]

    # features propres
    df = df[["PTS", "REB", "AST", "FG_PCT", "MIN"]].dropna()

    X = df.drop(columns=["PTS"])
    y = df["PTS"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test
