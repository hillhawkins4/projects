import random

items = ['rock', 'paper', 'scissors']

def player_answer():
    return input("What is your move? ")


def opponent_move():
    return random.choice(items)

opponent_move = opponent_move()
player_move = player_answer()

print("You chose:", player_move)
print("Opponent chose:", opponent_move)

if player_move == opponent_move:
    print("Tie")

elif player_move == "paper" and opponent_move == "rock":
    print("You win")

elif player_move == "rock" and opponent_move == "scissors":
    print("You win")

elif player_move == "scissors" and opponent_move == "paper":
    print("You win")

else :
    print("You lose")
