from flask import Flask, make_response, jsonify

app = Flask(__name__)

from tabletop_combat_manager.api.v1.game import game

app.register_blueprint(game)

@app.route('/')
def index():
    return "Hello, world!"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')