import random

print("WELCOME TO THE ROCK PAPER SCISSORS, SHOOT GAME!")    
print("-----------------------------------------------")

def get_player_choice():
    choices = ["Rock", "Paper", "Scissors"]

    print("Choose your weapon:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    print("Enter your choice (1, 2, 3): ", end="")
    while True:
            try:
                player = int(input())
                while player not in [1, 2, 3]:
                    print("Invalid choice! Please enter again: ", end="")
                    player = int(input())
                return choices[player - 1]
            except ValueError:
                print("Invalid input! Please enter a number: ", end="")

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print("-----------------------------------------------")
    print(f"You chose {player_choice}.")
    print(f"Computer chose {computer_choice}.")
    print("-----------------------------------------------")
    print(determine_winner(player_choice, computer_choice))

if __name__ == "__main__":
    play_game()

