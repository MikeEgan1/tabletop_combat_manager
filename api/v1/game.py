from flask import Flask, Blueprint

game = Blueprint('game', __name__)

@game.route('/hello')
def index():
    return "Hello, game!"