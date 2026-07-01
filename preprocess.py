# preprocess.py
import re # For regular expressions (e.g., removing URLs, special characters)
import nltk # Natural Language Toolkit for text processing tasks
import emoji # For handling and removing emojis from the text
import contractions # For expanding contractions (e.g., "don't" -> "do not")
from bs4 import BeautifulSoup # For parsing and removing HTML tags from the text
from nltk.tokenize import word_tokenize # For splitting text into individual words (tokens)
from nltk.corpus import stopwords # For removing common words that don't add much meaning (e.g., "the", "is")
from nltk.stem import WordNetLemmatizer # For converting words to their base/dictionary form (e.g., "running" -> "run")

# Download required NLTK resources (only needed once)
nltk.download("punkt", quiet=True) # Downloads the pre-trained tokenizer model
nltk.download("stopwords", quiet=True) # Downloads the standard list of English stop words
nltk.download("wordnet", quiet=True) # Downloads the WordNet database used for lemmatization
nltk.download("omw-1.4", quiet=True) # Downloads Open Multilingual Wordnet (required by WordNetLemmatizer in newer NLTK versions)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = emoji.replace_emoji(text, replace="")
    text = contractions.fix(text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    words = word_tokenize(text)
    words = [word for word in words if word.lower() not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    
    return " ".join(words)