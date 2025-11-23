import json
from werkzeug.wrappers import Response
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h3>Hola mundo!</h3>'

if __name__ == '__main__':
    # debug=True es opcional, pero útil cuando estás desarrollando
    app.run(debug=True)

