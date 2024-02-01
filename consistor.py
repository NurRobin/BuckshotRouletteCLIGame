# Global Variables for Lifes and Bullets

# Lifes for player 1 and 2
lifes_player = -1
lifes_dealer = -1
name_player = "Player"

def get_lifes_player():
    return lifes_player

def get_lifes_dealer():
    return lifes_dealer

def set_lifes_player(lifes):
    global lifes_player
    lifes_player = lifes
    
def set_lifes_dealer(lifes):
    global lifes_dealer
    lifes_dealer = lifes

def set_name_player(name):
    global name_player
    name_player = name

def get_name_player():
    return name_player

# Bullets
bullets = [2]
blanks = 0
lethals = 0

# Getters and Setters for Bullets


def get_blanks():
    return blanks

def get_lethals():
    return lethals

    
def set_bullets(bullet):
    global bullets
    bullets = bullet
    
def set_blanks(blank):
    global blanks
    blanks = blank
    
def set_lethals(life):
    global lethals
    lethals = life

# Items
items_player = []
items_dealer = []
saw_active = False
cuffs = 0
dealer_knows_bullet = 2

def get_items_player():
    return items_player

def get_items_dealer():
    return items_dealer

def set_items_player(items):
    global items_player
    items_player = items

def set_items_dealer(items):
    global items_dealer
    items_dealer = items

def set_saw_active(active):
    global saw_active
    saw_active = active

def get_saw_active():
    return saw_active

def set_cuffs(uses):
    global cuffs
    cuffs = uses

def get_cuffs():
    return cuffs

def set_dealer_knows_bullet(knows):
    global dealer_knows_bullet
    dealer_knows_bullet = knows

def get_dealer_knows_bullet():
    return dealer_knows_bullet