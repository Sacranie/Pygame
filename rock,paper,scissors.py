import random
import time 

options = ("rock", "paper", "scissors")

player = input('Choose rock, paper, or scissors: ')
while player not in options:
    player = input('Invalid choice. Please choose rock, paper, or scissors: ')
time.sleep(1)
computer = random.choice(options)
print(f"Computer chooses: {computer}")
time.sleep(1)
if computer == player:
    print('It\'s a draw!')
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print('You win!')
else:
    print('You lose!')
