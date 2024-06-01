import random

choices = ["Rock", "Paper", "Scissors"]
cpu_score = 0
player_score = 0

while True:
    player = input("Rock, Paper, Scissors, or End? ").capitalize()
    
    if player not in choices and player != "End":
        print("Invalid input. Please enter Rock, Paper, Scissors, or End.")
        continue
    
    if player == "End":
        print("Final Scores:")
        print(f"CPU: {cpu_score}")
        print(f"Player: {player_score}")
        break
    
    computer = random.choice(choices)
    
    if player == computer:
        print(f"Tie! Both chose {player}.")
    elif player == "Rock":
        if computer == "Paper":
            print(f"You lose! {computer} covers {player}.")
            cpu_score += 1
        else:
            print(f"You win! {player} smashes {computer}.")
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print(f"You lose! {computer} cut {player}.")
            cpu_score += 1
        else:
            print(f"You win! {player} covers {computer}.")
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print(f"You lose... {computer} smashes {player}.")
            cpu_score += 1
        else:
            print(f"You win! {player} cut {computer}.")
            player_score += 1
