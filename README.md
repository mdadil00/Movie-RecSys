# 🎬 Suggestaria - Movie Recommendation System

A collaborative filtering-based movie recommendation system that predicts user ratings and suggests similar movies.

🔗 **[Try the Live App Here](https://movie-recsys-qwaxbezq5fzrrxfyzv9dft.streamlit.app/)**

---

## 📂 Dataset Used

Sourced from Kaggle, comprising:
- `links.csv` – Maps platform IDs to `TmdbId`.
- `tmdb_5000_movies.csv` – Movie attributes (budget, genres, etc.).
- `tmdb_5000_credits.csv` – Cast and crew data.
- `ratings.csv` – User IDs, movie IDs, and their ratings.

> **Filtering:**  
> - Only movies rated by **250+ users** were included.  
> - Only users who rated **100+ movies** were retained.

---

## 🧹 Data Preprocessing

- Merged `movies` and `credits` on the **title** column.
- Checked and handled **missing values**.
- Converted necessary **data types**.
- Created a **user-movie pivot table** for collaborative filtering.

---

## 🧠 Algorithms & Key Functions

### 🔁 Movie-Based Collaborative Filtering
Uses cosine similarity to recommend similar movies and predict ratings.

---

### 🔍 `recommend(movie_name)`
Returns **top 5 similar movies**.

**Steps:**
1. Locate movie index.
2. Fetch similarity scores.
3. Sort scores.
4. Return top 5 similar movies.

---

### ⭐ `predict_rating(user, movie_name)`
Estimates user rating based on 5 similar movies.

**Steps:**
1. Retrieve average rating for the movie.
2. Get top 5 similar movies.
3. Compute weighted average of ratings.
4. Normalize score by similarity.
5. Handle edge cases (no similar ratings).

---

### 📈 `evaluate_model_with_sampling(sample_size)`
Evaluates performance using **Mean Absolute Error (MAE)** on random samples.

**MAE Achieved:** `0.8926`

---

## 📊 Performance Evaluation

- **MAE = 0.8926** implies ~0.89 rating points difference on a 1–5 scale.
- Indicates ~18% average error — moderate performance.

---

## 📸 Screenshots

<div align="center">
  <img src="Screenshots/Screenshot 2025-04-06 215637.png" alt="Prefer Dark Mode Please" width="400"/>
</div>
---

## 🧾 Conclusion

Suggestaria demonstrates a foundational implementation of collaborative filtering for movie recommendations. With a moderate MAE and meaningful recommendations, it sets the groundwork for more advanced and hybrid recommender systems.

---

## 💻 Deployment

Deployed using **Streamlit**.  
🔗 **[Access the Web App](https://movie-recsys-qwaxbezq5fzrrxfyzv9dft.streamlit.app/)**

---

## 📄 License

This project is for educational purposes.
