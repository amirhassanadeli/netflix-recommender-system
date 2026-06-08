---

# 🎬 Netflix Recommender System

A simple and interactive **Netflix Movie & Series Recommendation System** built with **Streamlit** and **Machine Learning (TF-IDF + Cosine Similarity)**.

This app recommends similar Netflix titles based on the description, genre, director, and cast of a selected movie or series.

---

## 🚀 Features

* 🔎 Search any Netflix movie or TV show
* 🎯 Get top 10 similar recommendations
* 🧠 Uses TF-IDF + Cosine Similarity for content-based filtering
* ⚡ Fast and lightweight Streamlit UI
* 📊 Uses Netflix dataset (`netflix_titles.csv`)

---

## 📸 Demo

> You can run the app locally and enter a title like:

```
Stranger Things
```

And receive similar Netflix recommendations instantly.

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎈
* Pandas 📊
* Scikit-learn 🤖

---

## 📂 Dataset

This project uses the **Netflix Titles Dataset** which includes:

* Title
* Description
* Genre (`listed_in`)
* Director
* Cast

Make sure the file below exists in your project directory:

```
netflix_titles.csv
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/amirhassanadeli/netflix-recommender-system.git
cd netflix-recommender
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, you can install manually:

```bash
pip install streamlit pandas scikit-learn
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. All text features are combined:

   * Description
   * Genre
   * Director
   * Cast

2. TF-IDF Vectorization converts text into numerical vectors.

3. Cosine Similarity measures similarity between movies.

4. Top 10 most similar titles are displayed.

---

## 📌 Example

Input:

```
Stranger Things
```

Output:

```
🍿 Dark
🍿 The OA
🍿 Black Mirror
...
```

---

## ⚠️ Notes

* Spelling must match exactly with dataset titles.
* If a title is not found, the app shows an error message.
* Dataset must not contain missing `title` values.

---

## 📈 Future Improvements

* Add fuzzy search (to handle typos)
* Use embeddings (Word2Vec / BERT)
* Add poster images
* Deploy on Streamlit Cloud / HuggingFace Spaces
* Add filter by genre/year

---

## 👨‍💻 Author

Built with ❤️ using Streamlit and Scikit-learn.

---

## 📜 License

This project is open-source and free to use for educational purposes.

---
