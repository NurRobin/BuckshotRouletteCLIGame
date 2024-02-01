import random
import consistor
import bullets

available_items = ["magnifying glass", "beer", "beer", "beer", "beer", "cigarettes", "cigarettes", "cigarettes", "saw", "cuffs"]

def new_items_player():
    items_player = consistor.get_items_player()
    items_player.append(random.choice(available_items))
    items_player.append(random.choice(available_items))
    items_player.append(random.choice(available_items))
    if len(items_player) > 8:
        # Shorten the list to 8 items
        items_player = items_player[:8]
    consistor.set_items_player(items_player)

def new_items_dealer():
    items_dealer = consistor.get_items_dealer()
    items_dealer.append(random.choice(available_items))
    items_dealer.append(random.choice(available_items))
    items_dealer.append(random.choice(available_items))
    if len(items_dealer) >= 8:
        # Shorten the list to 8 items
        items_dealer = items_dealer[:8]
    consistor.set_items_dealer(items_dealer)

def magnifying_glass():
    if bullets.get_current_bullet() == 1:
        return "lethal"
    elif bullets.get_current_bullet() == 0:
        return "blank"

def beer():
    bullets.ready_next_bullet()

def cigarettes(caller):
    if caller == "player":
        consistor.set_lifes_player(consistor.get_lifes_player() + 1)
    elif caller == "dealer":
        consistor.set_lifes_dealer(consistor.get_lifes_dealer() + 1)

def saw():
    consistor.set_saw_active(True)

def cuffs():
    consistor.set_cuffs(1)