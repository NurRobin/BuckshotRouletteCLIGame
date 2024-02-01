# Buckshot Roulette CLI Game (Updated)

Welcome to the Buckshot Roulette CLI Game! This is a fun and interactive command-line game. The game is based on the concept of 'Buckshot Roulette' by Mike Klubnika and is being developed by NurRobin.

## How to Play (Current Mechanics)

The game starts with a random number of bullets (between 3 and 7) loaded into a gun. Each bullet can be one of three types:

- Blank (0): This bullet is harmless.
- Lethal Round (1): This bullet takes away one life.

The bullets are shuffled at the start of each game, and the magazine is refilled every time it gets empty. The game continues until the player or the dealer loses all their lifse.

The player and the dealer start with 4 lifes each. 

## Game Files

The game consists of several Python files:

- `main.py`: This is the main file that runs the game. It handles the game loop and user interaction.
- `bullets.py`: This file manages the bullets in the game. It determines the type and order of the bullets at the start of each game and refills the magazine when it's empty.
- `consistor.py`: This file manages the global variables for the game, such as the number of lethals for the player and the dealer, and the current state of the bullets.
- `items.py`: This file is now functional and is used to add items to the game.

## Items in the Game

The game now includes items that can be used during the game.

## Running the Game

To run the game, simply execute the `main.py` file in a Python environment. The game will start automatically.

Please note that the game is still under development and may contain bugs or incomplete features. Your feedback and suggestions are welcome!

Enjoy the game and good luck!