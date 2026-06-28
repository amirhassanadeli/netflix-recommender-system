import os
import joblib

BASE_DIR = os.path.dirname(__file__)

df = joblib.load(
    os.path.join(BASE_DIR, "artifacts", "df.pkl")
)

indices = joblib.load(
    os.path.join(BASE_DIR, "artifacts", "indices.pkl")
)

cosine_sim = joblib.load(
    os.path.join(BASE_DIR, "artifacts", "cosine_sim.pkl")
)


def get_recommendations(title, top_n=10):

    if title not in indices:
        return None

    idx = indices[title]

    if hasattr(idx, "iloc"):
        idx = idx.iloc[0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:top_n + 1]

    movie_indices = [i[0] for i in sim_scores]

    return df["title"].iloc[movie_indices].tolist()