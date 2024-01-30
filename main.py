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
    
def print_top_left_and_right(left_text, right_text):
    columns = shutil.get_terminal_size().columns
    print(left_text.ljust(columns // 2) + right_text.rjust(columns // 2))

def main():
    clear_console()
    print_centered("A Buckshot Roulette CLI Game by")
    print_centered("by")
    print_centered("NurRobin")
    print_centered("Based on the game 'Buckshot Roulette'")
    print_centered("by")
    print_centered("Mike Klubnika")
    print_centered("Press Enter to continue")
    input()
    print_centered("Loading...")
    import consistor
    import bullets
    import items
    
    # Game Loop
    while True:
        bullets.new_game(random.randint(3, 7))
        consistor.set_lifes_player1(4)
        consistor.set_lifes_player2(4)
        clear_console()
        print_top_left_and_right("Player 1", "Player 2")
        print_top_left_and_right("Lifes: " + str(consistor.get_lifes_player1()), "Lifes: " + str(consistor.get_lifes_player2()))
        print("\n")
        # Print how many bullets are in the gun and how many are blanks and how many are lives
        print_centered("There are " + str(consistor.get_blanks()) + " blanks and " + str(consistor.get_lives()) + " lives.")
        print_centered("Press Enter to continue")
        input()

    
    
    
if __name__ == "__main__":
    main()    