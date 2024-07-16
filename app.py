from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = 'https://zenquotes.io/api/random'

@app.route('/')
def home():
    response = requests.get(API_URL)
    quote = response.json()[0]
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
