from flask import Flask, Blueprint

app = Flask(__name__)

game = Blueprint('game', __name__)

@app.route('/')
def index():
    return "Hello, world!"