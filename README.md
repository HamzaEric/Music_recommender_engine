📚 Music Recommender Engine


This is a machine learning-based recommender system that suggests relevant items based on user interactions. The model has been trained on a large dataset and uses pickle files for inference.

The Dataset used in this project is from kaggle[kaggle link](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)
---

## 🚀 How It Works

- Preprocessed data is fed into a recommendation algorithm (e.g., collaborative filtering or content-based).
- Trained models are serialized using `pickle` and used during inference.
- Large model files are **not stored in this GitHub repository** but are fetched dynamically at runtime from external storage.

---

## 📦 Files in This Repo

| File                | Description                               |
|---------------------|-------------------------------------------|
| `main.py`           | Main script to run the recommender logic  |
| `recommend.py`          | Backend logic                      |
| `requirements.txt`  | Python dependencies                       |
| `preprocessing.py`         | Backend preprocessing of the music data                      |

---

## 🧠 Model Files

Due to GitHub's 100MB file size limit, the trained model files are hosted externally.

- `cosine_sim.pkl` (700MB)
- `new_df.pkl` (69.7MB)


