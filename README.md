# IMDb Sentiment Analyzer

## 🌟 Overview
This project is an AI-powered web application that takes in IMDb-style movie reviews and predicts whether the sentiment is **Positive 😊** or **Negative 😞**. It leverages Natural Language Processing (NLP) and a highly optimized `Logistic Regression` model trained on 50,000 reviews to deliver real-time predictions. 

The application is fully containerized and production-ready for platforms like Render or Heroku.

<br/>

## ✨ Key Features & Workflow

### 1. Robust Machine Learning Engine
- **Model:** `Logistic Regression` fine-tuned and verified against multiple algorithms.
- **Accuracy:** `88.36%` on a strict train-test split.
- **Environment:** Trained on a clean environment using `scikit-learn==1.7.1` to completely eliminate version mismatch errors during deployment.

### 2. Advanced Text Preprocessing (NLP)
Before feeding any user input to the model, the text goes through a strict cleaning pipeline:
- Removes HTML tags (via BeautifulSoup).
- Cleans URLs, Emojis, and special characters.
- Expands English contractions (e.g., "don't" → "do not").
- Applies NLTK Tokenization, Stopwords removal, and Word Lemmatization.

### 3. Premium UI/UX Design
- Built with a modern **Glassmorphism** aesthetic.
- Fully responsive layout for Desktop and Mobile devices.
- Dynamic color-changing result cards (Green for Positive, Red for Negative) with micro-animations.

<br/>

## 📂 Project Structure (Deployment Ready)

To ensure fast and reliable cloud deployments, only the strictly necessary files are tracked in this repository:

```text
IMDB_Sentiment_Analysis/
├── models/
│   ├── sentiment_model.pkl       # Trained ML Model (Logistic Regression)
│   └── tfidf.pkl                 # Fitted TF-IDF Vectorizer
├── static/
│   └── css/
│       └── style.css             # Premium Glassmorphism UI Styling
├── templates/
│   └── index.html                # Main Frontend layout
├── app.py                        # Flask Backend Application
├── preprocess.py                 # Core text-cleaning module
├── requirements.txt              # Cloud Dependencies (Strict versions)
├── Procfile                      # Server startup command (Gunicorn)
└── README.md                     # Documentation
```
*(Note: Large datasets and rough experimentation notebooks are excluded to optimize server build time).*

<br/>

## 🚀 How to Run Locally

Follow these steps to get the project up and running on your local machine.

### 1. Clone the repository
```bash
git clone https://github.com/Shish-Kumar/IMDB_Sentiment_Analysis.git
cd IMDB_Sentiment_Analysis
```

### 2. Create a Virtual Environment (Highly Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the Web App
Open your favorite browser and navigate to:
👉 **http://127.0.0.1:5000/**

> **Note on NLTK Downloads:** The `preprocess.py` script automatically downloads required NLTK corpuses (`punkt`, `stopwords`, `wordnet`) the very first time you run the app. It might take a few extra seconds on the first run.

<br/>

## 🌐 Deployment Workflow (Render.com)

This project is perfectly configured to be deployed on **Render** for free:
1. Connect your GitHub account to Render.
2. Create a new **Web Service**.
3. Select this repository.
4. Set the **Build Command** to: `pip install -r requirements.txt`
5. Set the **Start Command** to: `gunicorn app:app`
6. Click **Deploy**. The `Procfile` and `requirements.txt` will automatically handle the rest!

<br/>

## 🤝 Acknowledgements

- Developed with ❤️ by **Shish Kumar Kushwah**.
- Dataset sourced from the public IMDb Movie Reviews repository.
