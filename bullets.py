import consistor
import random

def get_current_bullet():
    return consistor.bullets[0]

def ready_next_bullet():
    if consistor.bullets[0] != 2:
        consistor.bullets.pop(0)
    else:
        pass
    
def new_game(bullets):
    # new list with length of bullets
    bullets_list = []
    
    # Ensure there is at least one blank and one life bullet
    bullets_list.append(0)  # Add a blank bullet
    bullets_list.append(1)  # Add a life bullet

    # Fill the rest of the bullets randomly
    for i in range(bullets - 3):  # Subtract 3 because we've already added 2 bullets and we'll add the endgame bullet later
        bullets_list.append(random.randint(0, 1))

    random.shuffle(bullets_list)  # Shuffle the bullets to randomize their order

    # Ensure the last bullet is the endgame bullet
    bullets_list.append(2)

    consistor.set_bullets(bullets_list)
    # Number of blanks
    blanks = bullets_list.count(0)
    consistor.set_blanks(blanks)
    # Number of lives
    lives = bullets_list.count(1)
    consistor.set_lives(lives)