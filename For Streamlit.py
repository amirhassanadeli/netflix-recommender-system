import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎬 Netflix Recommender System")
st.write("Enter the name of your favorite Netflix movie or series to get 10 awesome suggestions!")


@st.cache_data
def load_data():
    df = pd.read_csv('netflix_titles.csv')
    df.fillna('', inplace=True)

    df['combined_features'] = df['description'] + ' ' + df['listed_in'] + ' ' + df['director'] + ' ' + df['cast']
    return df

df = load_data()

@st.cache_data
def calculate_similarity(data):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['combined_features'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

cosine_sim = calculate_similarity(df)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()


movie_title = st.text_input("Search for movie/series:", "Stranger Things")

if st.button("Recommender"):
    if movie_title in indices:
        idx = indices[movie_title]
        
        if isinstance(idx, pd.Series):
            idx = idx.iloc[0]
            
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        
        st.success("✅ Recommender For:")
        for title in df['title'].iloc[movie_indices].values:
            st.write(f"🍿 {title}")
    else:
        st.error("This movie wasn't in our database! Check the spelling.")
