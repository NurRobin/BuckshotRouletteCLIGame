# CLI Buckshot Game

import shutil
import os
import time
import random

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text):
    columns = shutil.get_terminal_size().columns
    print(text.center(columns))

def print_top_left(text):
    columns = shutil.get_terminal_size().columns
    print(text.ljust(columns))
    
def print_top_right(text):
    columns = shutil.get_terminal_size().columns
    print(text.rjust(columns))

def main():
    print_centered("A Buckshot Roulette CLI Game")
    print_centered("by")
    print_centered("NurRobin")
    print_centered("Based on the game 'Buckshot Roulette' by")
    print_centered("Mike Klubnika")
    print_centered("Press Enter to continue")
    input()
    print_centered("Loading...")
    import consistor
    import bullets
    import items
    
    # Game Loop
    while True:
        clear_console()
        consistor.set_lifes_player1(4)
        consistor.set_lifes_player2(4)
        bullets.new_game(random.randint(3, 7))
        print_top_left("Player 1")
        print_top_right("Player 2")
        print_top_left("Lifes: " + str(consistor.get_lifes_player1()))
        print_top_right("Lifes: " + str(consistor.get_lifes_player2()))
        # Print how many bullets are in the gun and how many are blanks and how many are lives
        print_centered("There are " + str(consistor.get_blanks()) + " blanks and " + str(consistor.get_lives()) + " lives in the gun.")
        print_centered("Press Enter to continue")
        input()

    
    
    
if __name__ == "__main__":
    main()    