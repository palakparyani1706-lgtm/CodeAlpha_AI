#pip install flask nltk scikit-learn(Terminal)

import nltk
import string
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

nltk.download('punkt_tab') 
nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.isalnum()]
    tokens = [w for w in tokens if w not in stopwords.words('english')]
    return " ".join(tokens)