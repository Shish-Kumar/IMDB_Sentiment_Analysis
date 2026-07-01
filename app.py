# app.py
import os # For interacting with the operating system (e.g., handling file paths)
import pickle # For loading the pre-trained machine learning model and vectorizer (.pkl files)
from flask import Flask, render_template, request, redirect, url_for, flash # Flask core components for routing, rendering HTML, handling requests, and showing alerts
from preprocess import preprocess_text  # Custom function to clean user input before prediction

app = Flask(__name__)
# Secret key is required for session management and flash messages
app.secret_key = "supersecretkeyformlproject"

# ---------- Safe Model Loading (Error Handling) ----------
try:
    # Models are expected inside the 'models/' directory
    model = pickle.load(open("models/sentiment_model.pkl", "rb"))
    vectorizer = pickle.load(open("models/tfidf.pkl", "rb"))
    print(" Models loaded successfully!")
except Exception as e:
    print(f" Error loading models: {e}")
    model = None
    vectorizer = None


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        # Retrieve and clean input text
        review = request.form.get("review", "").strip()

        # 1. Validation (Check for empty input)
        if not review:
            flash("Please enter a review for prediction!", "danger")
            return redirect(url_for("home"))

        # 2. Error Handling (Check if models failed to load)
        if model is None or vectorizer is None:
            flash("Server Error: Models are not loaded. Please try again later.", "danger")
            return redirect(url_for("home"))

        try:
            # 3. Core Prediction Process
            cleaned_review = preprocess_text(review)
            review_vector = vectorizer.transform([cleaned_review])
            result = model.predict(review_vector)

            # Determine sentiment outcome
            if result[0] == "positive":
                prediction = "😊 Positive Review"
            else:
                prediction = "😞 Negative Review"
                
            flash("Prediction completed successfully!", "success")

        except Exception as e:
            flash(f"An error occurred during prediction: {e}", "danger")
            return redirect(url_for("home"))

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)