import random
import time
import os
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

choices = ["🪨 Rock", "📜 Paper", "🗡️ Scissors"]

def get_player_choice():
    try:
        player = int(input())
        if player in [1, 2, 3]:
            return player - 1
        return -1
    except ValueError:
        return None

def get_computer_choice():
    return random.randint(0, 2)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "🤝 It's a tie!"
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        return "🎉 You win!"
    else:
        return "😢 Computer wins!"

def play_game():
    colors = [Fore.RED, Fore.GREEN, Fore.BLUE]
    ascii_text = pyfiglet.figlet_format("Rock Paper Scissors", font="small")
    lines = ascii_text.split("\n")
    for i, line in enumerate(lines):
        print(colors[i % len(colors)] + line)

    print(Fore.WHITE + "-----------------------------------------------")
    rainbow_colors = [Fore.RED, Fore.LIGHTRED_EX, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

    text = "WELCOME TO THE ROCK PAPER SCISSORS, SHOOT GAME!"
    rainbow_text = "".join(random.choice(rainbow_colors) + char for char in text)

    print(rainbow_text + Style.RESET_ALL)   
    print(Fore.WHITE + "-----------------------------------------------")

    print("Choose your weapon:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    print("Enter your choice (1, 2, 3): ", end="")
    player_choice = get_player_choice()
    while player_choice is None or player_choice == -1:
        if player_choice is None:
            print(Fore.RED + "Invalid input! Please enter again: ", end="")
        elif player_choice == -1:
            print(Fore.RED + "Invalid choice! Please enter again: ", end="")
        player_choice = get_player_choice()
    
    computer_choice = get_computer_choice()

    print(Fore.MAGENTA + "-----------------------------------------------")
    colors = [Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTRED_EX]
    words = ["Rock", "Paper", "Scissors"]

    for i, word in enumerate(words):
        print(f"{colors[i]}{word}...", end="", flush=True)
        time.sleep(0.25)

    print(Fore.MAGENTA + " SHOOT!")
    time.sleep(0.5)

    print(Fore.CYAN + "-----------------------------------------------")

    print(f"You chose {choices[player_choice].split()[0]}.")
    print(f"Computer chose {choices[computer_choice].split()[0]}.")
    print(Fore.CYAN + "-----------------------------------------------")

    time.sleep(0.5)
    print(determine_winner(player_choice, computer_choice))

if __name__ == "__main__":
    play_game()