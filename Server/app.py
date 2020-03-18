from flask import Flask, request, jsonify
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    data = " Donkey"
    return jsonify({'data': data})


def clean_text(a):
    text = re.sub('[^a-zA-Z0-9]', ' ', a)
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [WordNetLemmatizer().lemmatize(word) for word in text if word not in (stopwords.words('english'))]
    text = ' '.join(text)
    return text


@app.route('/verify', methods=['POST'])
def check():
    message = request.form.get('message')
    with open('../Model/spamClassifier.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('../Model/count_vect', 'rb') as f:
        vectorizer = pickle.load(f)
    if model.predict(vectorizer.transform([clean_text(message)])):
        return jsonify({'data': 'spam'})
    else:
        return jsonify({'data': 'not spam'})


if __name__ == '__main__':
    print("starting flask server")
    app.run(debug=True)
