from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/game')
def index():
    return render_template('index.html', title='Home', game=game)

@app.route("/events", methods="POST")
def play_game(player_choice, com_choice):
    player_choice = input("Shoot!:")
    pchoice = player_choice.lower()
    com_choice = random.choice(com_options)
    if pchoice == "rock" and com_choice == "scissors":
        return "YOU WIN!"
    elif pchoice == "paper" and com_choice == "rock":
        return "YOU WIN!"
    elif pchoice == "scissors" and com_choice == "paper":
            return "YOU WIN!"
    elif pchoice == com_choice:
            return "IT'S A TIE"
    else:
        return "You lose"




