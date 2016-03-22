from flask import Flask, Blueprint, jsonify
from tabletop_combat_manager.game.builder import Builder as GameBuilder
from tabletop_combat_manager.game.creator import Creator as GameCreator
from tabletop_combat_manager.creature.builder import Builder as CreatureBuilder

game = Blueprint('game', __name__)

@game.route('/game/hello')
def index():
    return "Hello, game!"

@game.route('/game/new_game', methods=['GET'])
def new_game():
    builder = GameBuilder()

    game = builder.build()
    return jsonify(game.json())

@game.route('/game/<string:game_id>/add_player', methods=['POST'])
def add_player(game_id):
    creator = GameCreator()
    builder = CreatureBuilder()

    player = builder.setName(request.json['name']).build()
    game = creator.get(game_id)
    game.add_player(player)

    return jsonify(game.json())