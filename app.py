from flask import Flask, render_template
from models.game import Game
from models.player import * 
app = Flask(__name__)

# from controllers import controller

@app.route("/play_game/<choice1>/<choice2>")
def play(choice1, choice2):
    player1 = Player("Player1", choice1)
    player2 = Player("Player2", choice2)
    Game.play_game(player1, player2)
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)