# settings.py

FPS = 60
GAME_MAP = "data/mspacman.txt"
GAME_MAP = "data/pacman.txt"

TILE_SIZE = 32
PELLET_SIZE = 3
SCORE_OFFSET = 0
SHOW_NAMES = True

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Collision radius
GHOST_COLLISION_RADIUS = 400
PELLET_COLLISION_RADIUS = 200

# Game Balance
GHOST_SPEED = 2
PLAYER_SPEED = 2
PELLET_SCORE = 10

# SFX
BGM_SFX = "data/bgm-blues.mp3"
EAT_PELLET_SFX = "data/chomp.mp3"
POWER_PILL_SFX = "data/powerpill.mp3"
DEATH_SFX = "data/sad_trumpet.mp3"
