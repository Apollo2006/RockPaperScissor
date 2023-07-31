import tkinter as tk
import random

# create a window
window = tk.Tk()
window.geometry("500x400")

player_score = 0
computer_score = 0

# This function will randomly choose one option which is the computer's move.
def get_computers_choice():
  return random.choice(["rock", "paper", "scissor"])

# Determines who wins when player makes a choice
def determine_winner(computers_choice, players_choice):
  global player_score, computer_score
  
  if players_choice == computers_choice:
    return "It's a tie"
  elif (players_choice == "rock" and computers_choice == "scissor") or \
       (players_choice == "paper" and computers_choice == "rock") or \
       (players_choice == "scissor" and computers_choice == "paper"):
       player_score += 1
       return "You win"
  else:
    computer_score += 1
    return "You LOST!"

def play_game(player_choice):
  computers_choice = get_computers_choice()
  result = determine_winner(player_choice, computers_choice)
  result_label.config(text=f"AI chose {computers_choice}.\n{result}")
  update_scorebaord()

def on_rock():
  play_game("rock")
def on_paper():
  play_game("paper")
def on_scissor():
  play_game("scissor")

def update_scorebaord():
  scoreboard_label.config(text=f"Player: {player_score} | Computer: {computer_score}")

rock_button = tk.Button(window, text="Rock", command=on_rock)
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(window, text="Paper", command=on_paper)
paper_button.pack(side=tk.LEFT, padx=10)

scissor_button = tk.Button(window, text="Scissor", command=on_scissor)
scissor_button.pack(side=tk.LEFT, padx=10)
  
result_label = tk.Label(window, text="Choose Your move!")
result_label.pack(pady=50)

scoreboard_label = tk.Label(window, text="Player: 0 | AI: 0")
scoreboard_label.pack()

window.mainloop()
