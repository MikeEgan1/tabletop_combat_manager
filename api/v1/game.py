from flask import Flask, Blueprint, jsonify
from tabletop_combat_manager.game import create_new_game

game = Blueprint('game', __name__)

@game.route('/game/hello')
def index():
    return "Hello, game!"

@game.route('/game/new_game')
def new_game():
    return jsonify({'id' : create_new_game()})

