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

def print_and_sleep(*args):
    for arg in args:
        print_centered(arg)
        time.sleep(1)

class GameState:
    def __init__(self):
        self.state = "Intro"
        self.consistor = __import__('consistor')
        self.bullets = __import__('bullets')
        self.items = __import__('items')

    def next_state(self):
        if self.state == "Intro":
            self.state = "Game"
        elif self.state == "Game":
            self.state = "Game"

    def run(self):
        if self.state == "Intro":
            self.intro()
        elif self.state == "Game":
            self.game()

    def intro(self):
        clear_console()
        print_centered("A Buckshot Roulette CLI Game")
        print_centered("by")
        print_centered("NurRobin")
        print_centered("Based on the game 'Buckshot Roulette'")
        print_centered("by")
        print_centered("Mike Klubnika")
        print_centered("Press Enter to continue")
        input()
        print_centered("Loading...")
        time.sleep(1)
        clear_console()
        print_centered("Whats your name?")
        self.consistor.set_name_player(input())
        clear_console()

    def game(self):
        self.bullets.new_mag(random.randint(3, 9))
        self.consistor.set_lifes_player(4)
        self.consistor.set_lifes_dealer(4)
        clear_console()
        print_top_left_and_right(self.consistor.get_name_player(), "Dealer")
        print_top_left_and_right("Lifes: " + str(self.consistor.get_lifes_player()), "Lifes: " + str(self.consistor.get_lifes_dealer()))
        print("\n")
        # Print how many bullets are in the gun and how many are blanks and how many are lethals
        print_centered("There are " + str(self.consistor.get_blanks()) + " blanks and " + str(self.consistor.get_lethals()) + " lethals.")
        print_centered("Press Enter to continue")
        input()
        clear_console()
        print_centered("The dealer loads the gun and hands it to you.")
        time.sleep(2)
        self.players_turn()


    def shoot(self, shooter, target):
        is_lethal = self.bullets.get_current_bullet() == 1
        self.shoot_target(shooter, target, is_lethal)

    def shoot_target(self, shooter, target, is_lethal):
        lifes = self.consistor.get_lifes(target)
        lifes -= 2 if self.consistor.get_saw_active() else 1 if is_lethal else 0
        self.consistor.set_lifes(target, lifes)
        self.consistor.set_lethals(self.consistor.get_lethals() - 1 if is_lethal else self.consistor.get_lethals())
        self.consistor.set_blanks(self.consistor.get_blanks() - 1 if not is_lethal else self.consistor.get_blanks())

        if shooter == target:
            message = "The Dealer aims at itself..." if shooter == "Dealer" else "You aim at yourself..."
        else:
            message = "You aim at the Dealer..." if shooter == "Player" else "The Dealer aims at you..."

        if is_lethal:
            action = "...and shoot!" if shooter == "Player" else "...and shoots!"
            hit_message = "The Dealer is hit!" if shooter == "Player" else "You are hit!"
            print_and_sleep(message, action)
            print_and_sleep(hit_message)
        else:
            action = "...and shoot!" if shooter == "Player" else "...and shoots!"
            print_and_sleep(message, action, "It's a blank!")

        self.consistor.set_saw_active(False)
        self.check_lifes(target)
        self.next_turn(target)

    def check_lifes(self, target):
        lifes = self.consistor.get_lifes(target)
        if lifes <= 0:
            self.win() if target == "Dealer" else self.lose()
        else:
            print_and_sleep(f"{target} has {lifes} lifes left.")

    def next_turn(self, next_caller, cuff_call=False):
        clear_console()
        self.bullets.ready_next_bullet()
        if not cuff_call and self.consistor.get_cuffs() > 0:
            self.consistor.set_cuffs(self.consistor.get_cuffs() - 1)
            print_centered(f"{next_caller} is restrained!")
            time.sleep(2)
            self.next_turn("Player" if next_caller == "Dealer" else "Dealer", True)
        else:
            self.dealers_turn() if next_caller == "Dealer" else self.players_turn()

    def game_over(self, message, next_state):
        clear_console()
        print_centered(message)
        print_centered("Press Enter to continue")
        print_centered("Press Escape to quit")
        choice = input()
        if choice.lower() == "escape":
            exit()
        else:
            next_state()

    def win(self):
        self.game_over("You won!", self.game)

    def lose(self):
        self.game_over("You lost!", self.next_state)

    def players_turn(self, new_items=True):
        if new_items:
            self.items.new_items_player()
        if self.bullets.get_current_bullet() == 2:
            clear_console()
            print_centered("The gun is empty!")
            time.sleep(1)
            print_centered("The dealer loads the gun anew.")
            self.bullets.new_mag(random.randint(3, 9))
            time.sleep(1)
            clear_console()
            print_top_left_and_right(self.consistor.get_name_player(), "Dealer")
            print_top_left_and_right("Lifes: " + str(self.consistor.get_lifes_player()), "Lifes: " + str(self.consistor.get_lifes_dealer()))
            print("\n")
            print_centered("There are " + str(self.consistor.get_blanks()) + " blanks and " + str(self.consistor.get_lethals()) + " lethals.")
            print_centered("Press Enter to continue")
            input()
            clear_console()
            print_centered("The dealer hands the gun to you.")
            time.sleep(2)
            clear_console()
        print_top_left_and_right(self.consistor.get_name_player(), "Dealer")
        print_top_left_and_right("Lifes: " + str(self.consistor.get_lifes_player()), "Lifes: " + str(self.consistor.get_lifes_dealer()))
        print("\n")
        print_centered("What do you want to do?")
        print_centered("1. Shoot the Dealer")
        print_centered("2. Shoot yourself")
        print_centered("3. Check your items")

        # Get the user's choice
        choice = input()
        clear_console()
        if choice == "1":
            self.shoot("Player", "Dealer")
        elif choice == "2":
            self.shoot("Player", "Player")
        elif choice == "3":
            self.items_menu()
        else:
            print_centered("Invalid input!")
            time.sleep(1)
            clear_console()

    def dealers_turn(self, new_items=True):
        if new_items:
            self.items.new_items_dealer()
        if self.bullets.get_current_bullet() == 2:
            clear_console()
            print_centered("The gun is empty!")
            time.sleep(1)
            print_centered("The dealer loads the gun anew.")
            self.bullets.new_mag(random.randint(3, 9))
            time.sleep(1)
            clear_console()
            print_top_left_and_right(self.consistor.get_name_player(), "Dealer")
            print_top_left_and_right("Lifes: " + str(self.consistor.get_lifes_player()), "Lifes: " + str(self.consistor.get_lifes_dealer()))
            print("\n")
            print_centered("There are " + str(self.consistor.get_blanks()) + " blanks and " + str(self.consistor.get_lethals()) + " lethals.")
            print_centered("Press Enter to continue")
            input()
            clear_console()
        print_centered("The dealer is thinking...")
        time.sleep(2)
        if self.consistor.get_items_dealer() != []:
            if "cigarettes" in self.consistor.get_items_dealer():
                clear_console()
                print_centered("The dealer smokes a cigarette and gains one life.")
                self.items.cigarettes("dealer")
                time.sleep(2)
                clear_console()
                self.remove_item("dealer", "cigarettes")
                self.dealers_turn(False)
            elif "magnifying glass" in self.consistor.get_items_dealer() and self.consistor.get_dealer_knows_bullet() == 2:
                clear_console()
                print_centered("The dealer uses the magnifying glass.")
                time.sleep(1)
                clear_console()
                print_centered("The dealer looks at the bullet...")
                time.sleep(2)
                clear_console()
                self.consistor.set_dealer_knows_bullet(self.bullets.get_current_bullet())
                self.remove_item("dealer", "magnifying glass")
                self.dealers_turn(False)
            elif "beer" in self.consistor.get_items_dealer() and self.consistor.get_dealer_knows_bullet() == 2 and self.consistor.get_lethals() < self.consistor.get_blanks():
                clear_console()
                print_centered("The dealer drinks the beer and empties one bullet.")
                self.items.beer()
                time.sleep(2)
                clear_console()
                self.remove_item("dealer", "beer")
                self.dealers_turn(False)
            elif "cuffs" in self.consistor.get_items_dealer() and self.consistor.get_dealer_knows_bullet() == 1:
                clear_console()
                print_centered("The dealer uses the cuffs, restraining you for two turns.")
                self.items.cuffs()
                time.sleep(2)
                clear_console()
                self.remove_item("dealer", "cuffs")
                self.dealers_turn(False)
            elif "saw" in self.consistor.get_items_dealer() and self.consistor.get_dealer_knows_bullet() == 1:
                self.consistor.set_saw_active(True)
                self.remove_item("dealer", "saw")
                self.consistor.set_dealer_knows_bullet(2)
                self.shoot("Dealer", "Player")
        clear_console()
        if self.consistor.get_dealer_knows_bullet() == 0:
            self.consistor.set_dealer_knows_bullet(2)
            self.shoot("Dealer", "Dealer")
        elif self.consistor.get_dealer_knows_bullet() == 1:
            self.consistor.set_dealer_knows_bullet(2)
            self.shoot("Dealer", "Player")
        elif self.consistor.get_dealer_knows_bullet() == 2:
            if self.consistor.get_lethals() > self.consistor.get_blanks():
                self.consistor.set_dealer_knows_bullet(2)
                self.shoot("Dealer", "Player")
            else:
                self.consistor.set_dealer_knows_bullet(2)
                self.shoot("Dealer", "Dealer")

    def items_menu(self):
        clear_console()
        print_centered("Your items:")
        for item in self.consistor.get_items_player():
            print_centered(item)
        print_centered("Press Enter to continue")
        input()
        clear_console()
        print_centered("What do you want to do?")
        print_centered("1. Use Magnifying Glass")
        print_centered("2. Use Beer")
        print_centered("3. Use Cigarettes")
        print_centered("4. Use Saw")
        print_centered("5. Use Cuffs")
        print_centered("6. Go back")
        choice = input()
        clear_console()
        if choice == "1":
            self.use_magnifying_glass()
        elif choice == "2":
            self.use_beer()
        elif choice == "3":
            self.use_cigarettes()
        elif choice == "4":
            self.use_saw()
        elif choice == "5":
            self.use_cuffs()
        elif choice == "6":
            self.players_turn(False)
        else:
            print_centered("Invalid input!")
            time.sleep(1)
            clear_console()
            self.items_menu()

    def use_magnifying_glass(self):
        allowed = self.check_if_player_has_item("magnifying glass")
        if allowed == False:
            print_centered("You don't have a magnifying glass!")
            time.sleep(1)
            self.items_menu()
        clear_console()
        print_centered("You use the magnifying glass.")
        time.sleep(1)
        clear_console()
        print_centered("You look at the bullet...")
        time.sleep(2)
        clear_console()
        print_centered("It's a " + self.items.magnifying_glass() + " bullet!")
        time.sleep(2)
        clear_console()
        self.remove_item("player", "magnifying glass")
        self.items_menu()

    def use_beer(self):
        allowed = self.check_if_player_has_item("beer")
        if allowed == False:
            print_centered("You don't have a beer!")
            time.sleep(1)
            self.items_menu()
        clear_console()
        print_centered("You drink the beer and empty one bullet.")
        print_centered("It was a " + self.items.magnifying_glass() + " bullet!")
        self.items.beer()
        time.sleep(2)
        clear_console()
        self.remove_item("player", "beer")
        self.items_menu()

    def use_cigarettes(self):
        allowed = self.check_if_player_has_item("cigarettes")
        if allowed == False:
            print_centered("You don't have cigarettes!")
            time.sleep(1)
            self.items_menu()
        clear_console()
        print_centered("You smoke a cigarette and gain one life.")
        self.items.cigarettes("player")
        time.sleep(2)
        clear_console()
        self.remove_item("player", "cigarettes")
        self.items_menu()

    def use_saw(self):
        allowed = self.check_if_player_has_item("saw")
        if allowed == False:
            print_centered("You don't have a saw!")
            time.sleep(1)
            self.items_menu()
        clear_console()
        print_centered("You use the saw, making the next bullet do double damage.")
        self.items.saw()
        time.sleep(2)
        clear_console()
        self.remove_item("player", "saw")
        self.items_menu()

    def use_cuffs(self):
        allowed = self.check_if_player_has_item("cuffs")
        if allowed == False:
            print_centered("You don't have cuffs!")
            time.sleep(1)
            self.items_menu()
        clear_console()
        print_centered("You use the cuffs, restraining the dealer for two turns.")
        self.items.cuffs()
        time.sleep(2)
        clear_console()
        self.remove_item("player", "cuffs")
        self.items_menu()

    def remove_item(self, caller, item):
        if caller == "player":
            items = self.consistor.get_items_player()
            items.remove(item)
            self.consistor.set_items_player(items)
        elif caller == "dealer":
            items = self.consistor.get_items_dealer()
            items.remove(item)
            self.consistor.set_items_dealer(items)
    def check_if_player_has_item(self, item):
        if item in self.consistor.get_items_player():
            return True
        else:
            return False

def main():
    game = GameState()
    while True:
        game.run()
        game.next_state()

if __name__ == "__main__":
    main()