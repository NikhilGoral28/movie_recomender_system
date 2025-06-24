# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**, a content-based recommendation engine that suggests movies based on user preferences using Natural Language Processing (NLP) and cosine similarity.


---

## 📌 Features

- 🔍 **Search Movies** by title.
- 🧠 **Recommends Similar Movies** using content-based filtering.
- 📚 Based on **movie metadata** (genres, keywords, overview).
- 🚀 Lightweight and fast predictions using **cosine similarity**.
- 🌐 Simple and intuitive **Flask web interface**.

---

## 🧠 How It Works

1. **Data Preprocessing**: Merged metadata from TMDB (title, genres, overview).
2. **Vectorization**: vectorizer creates movie vectors.
3. **Similarity Matrix**: Cosine similarity finds nearest movies.
4. **Recommendation**: Top 10 similar movies returned for any given title.

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3.8+
- pip

### Download Model Files

📥 Download Pre-trained Model Files
Download the following .pkl files and place them in the model/ directory:

🔗 [cosine_sim.pkl](https://drive.google.com/file/d/18i3UuI_WYSybm5Au-tzGXMgh9E-1sQIO/view?usp=drive_link) 

🔗 [final_movies.pkl](https://drive.google.com/file/d/1yulsSv5ifyIM1m_j7FIi41x333zBgIy1/view?usp=drive_link) 

⚠️ Make sure the model/ folder exists and both files are placed correctly inside it.

# Example folder structure
model/
├── cosine_sim.pkl
└── final_movies.pkl

▶️**Run the App**
python app.py

🙋‍♂️ **Author**
Nikhil Goral
📧 nikhilgoral587@gmail.com
🌐 [LinkedIn](https://www.linkedin.com/in/nikhil-goral-340266259)

