from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS, cross_origin
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


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
        return jsonify({'data': 'Spam Message!!', 'code': 1})
    else:
        return jsonify({'data': 'Non Spam Message!!', 'code': 0})


if __name__ == '__main__':
    print("starting flask server")
    app.run(debug=True)
