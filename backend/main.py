from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})


@app.route('/')
def home():
    return ("Hello, world")


if __name__=="__main__":
    app.run(debug=True )