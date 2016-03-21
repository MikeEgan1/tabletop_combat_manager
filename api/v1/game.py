from flask import Flask, Blueprint, jsonify
from tabletop_combat_manager.game.builder import Builder

game = Blueprint('game', __name__)

@game.route('/game/hello')
def index():
    return "Hello, game!"

@game.route('/game/new_game')
def new_game():
    builder = Builder()

    game = builder.build()
    return jsonify(game.json())

@game.route('/game/<string:game_id>/add_player')
def add_player():
    pass