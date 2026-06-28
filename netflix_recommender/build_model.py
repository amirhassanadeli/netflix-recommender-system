# build_model.py

import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/netflix_titles.csv")
df.fillna("", inplace=True)

df["combined_features"] = (
    df["description"]
    + " "
    + df["listed_in"]
    + " "
    + df["director"]
    + " "
    + df["cast"]
)

tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(tfidf_matrix)

indices = pd.Series(
    df.index,
    index=df["title"]
).drop_duplicates()

joblib.dump(df, "artifacts/df.pkl")
joblib.dump(indices, "artifacts/indices.pkl")
joblib.dump(cosine_sim, "artifacts/cosine_sim.pkl")

print("Model built successfully")