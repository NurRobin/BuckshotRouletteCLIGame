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

    # Calculate the number of remaining bullets
    remaining_bullets = bullets - 3  # Subtract 3 because we've already added 2 bullets and we'll add the endgame bullet later

    # Calculate the number of blanks and lives based on the desired percentages
    blanks = int(remaining_bullets * random.uniform(0.4, 0.6))  # 20-50% blanks
    lives = remaining_bullets - blanks

    # Add the blanks and lives to the bullet list
    bullets_list.extend([0] * blanks)
    bullets_list.extend([1] * lives)

    random.shuffle(bullets_list)  # Shuffle the bullets to randomize their order

    # Ensure the last bullet is the endgame bullet
    bullets_list.append(2)

    consistor.set_bullets(bullets_list)
    # Number of blanks
    consistor.set_blanks(bullets_list.count(0))
    # Number of lives
    consistor.set_lives(bullets_list.count(1))