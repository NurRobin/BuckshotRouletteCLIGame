# Global Variables for Lifes and Bullets

# Lifes for player 1 and 2
lifes_player1 = -1
lifes_player2 = -1

def get_lifes_player1():
    return lifes_player1

def get_lifes_player2():
    return lifes_player2

def set_lifes_player1(lifes):
    global lifes_player1
    lifes_player1 = lifes
    
def set_lifes_player2(lifes):
    global lifes_player2
    lifes_player2 = lifes

# Bullets
bullets = [2]
blanks = 0
lives = 0

# Getters and Setters for Bullets


def get_blanks():
    return blanks

def get_lives():
    return lives

    
def set_bullets(bullet):
    global bullets
    bullets = bullet
    
def set_blanks(blank):
    global blanks
    blanks = blank
    
def set_lives(life):
    global lives
    lives = life