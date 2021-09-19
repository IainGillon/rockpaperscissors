from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/game')
def index():
    return render_template('index.html', title='Home', game=game)

# @app.route("game", methods="POST")

# def play_game(self):
#     player_details = []
#     player_details = Player.get_player_name_and_choice()
#     print(player_details)
#     player1_name = player_details[0]
#     player2_name = player_details[1]
#     player1_choice = player_details[2]
#     player2_choice = player_details[3]
#     if player1_choice == "rock" and player2_choice == "scissors":
#         print('The winner is player 1')
#         return player1_name

#     elif  player2_choice == "rock" and player1_choice == "scissors":
#         print('The winner is player 2')
#         return player2_name
#     elif player1_choice == "paper" and player2_choice == "rock":
#         print("The winner is player1")
#         return player1_name
#     elif player2_choice == "paper" and player1_choice == "rock":
#         print("the winner is player 2")
#         return player2_name
#     elif player1_choice == "scissors" and player2_choice == "paper":
#         print("Player 1 wins")
#         return player1_name
#     elif player2_choice == "scissors" and player1_choice == "paper":
#         print("Player 2 wins")
#         return player2_name
        
#     elif player1_choice == player2_choice:
#         print("IT'S A TIE")
#         return "IT'S A TIE" 
            
#     else:
#         return "Error"
#     return render_template("index.html", title='home', game=game  )