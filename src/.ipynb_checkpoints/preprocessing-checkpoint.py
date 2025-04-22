import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Baixar recursos do NLTK
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # 1. Coloca em lowercase
    text = text.lower()
    # 2. Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    # 3. Remove pontuações
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 4. Tokeniza
    tokens = nltk.word_tokenize(text)
    # 5. Remove stopwords e lematiza
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    # 6. Junta de novo
    return ' '.join(tokens)