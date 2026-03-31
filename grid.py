# grid.py

import pygame
from settings import TILE_SIZE, PELLET_COLLISION_RADIUS, PELLET_SIZE, GAME_MAP


# Traditional pac-man grid with pellets and walls
# # = wall
# . = pellet
# G = ghost spawn zone (will do this later)
# E = empty space (will do this later)
# P = power pellet (will do this later)
# TODO: Load this from a file
# TILE_MAP = [
#    "............##............",
#    ".####.#####.##.#####.####.",
#    "P####.#####.##.#####.####P",
#    ".####.#####.##.#####.####.",
#    "..........................",
#    ".####.##.########.##.####.",
#    ".####.##.########.##.####.",
#    "......##....##....##......",
#    "#####.#####E##E#####.#####",
#    "#####.#####E##E#####.#####",
#    "#####.##EEEEEEEEEE##.#####",
#    "#####.##E###GG###E##.#####",
#    "#####.##E#GGGGGG#E##.#####",
#    "EEEEE.EEE#GGGGGG#EEE.EEEEE",
#    "#####.##E#GGGGGG#E##.#####",
#    "#####.##E########E##.#####",
#    "#####.##EEEEEEEEEE##.#####",
#    "#####.##E########E##.#####",
#    "#####.##E########E##.#####",
#    "............##............",
#    ".####.#####.##.#####.####.",
#    ".####.#####.##.#####.####.",
#    "P..##................##..P",
#    "##.##.##.########.##.##.##",
#    "##.##.##.########.##.##.##",
#    "......##....##....##......",
#    ".##########.##.##########.",
#    ".##########.##.##########.",
#    ".........................."
#]


class Grid:
    def __init__(self, mapcolor, pelletcolor):
        self.map = []
        self.pellets = []
        self.walls = []
        self.mapcolor = mapcolor
        self.pelletcolor = pelletcolor

        self.import_map(GAME_MAP)
        self.create_grid()


    def create_grid(self):
        # Create walls and pellets based on the map
        for row_index, row in enumerate(self.map):
            for col_index, tile in enumerate(row):
                if tile == ".":
                    # Center the pellet in the tile
                    x = col_index * TILE_SIZE + TILE_SIZE // 2
                    y = row_index * TILE_SIZE + TILE_SIZE // 2
                    self.pellets.append((x, y))
                elif tile == "#":
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    self.walls.append((x, y))



    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, self.mapcolor, (wall[0], wall[1], TILE_SIZE, TILE_SIZE))

        for pellet in self.pellets:
            pygame.draw.circle(screen, self.pelletcolor, pellet, PELLET_SIZE)


    def is_wall(self, x, y):
        col = int(x // TILE_SIZE)
        row = int(y // TILE_SIZE)

        if row < 0 or row >= len(self.map):
            return True
        if col < 0 or col >= len(self.map[0]):
            return True
        return self.map[row][col] == "#"
    

    def check_collision(self, player):
        for pellet in self.pellets[:]:
            if (player.x - pellet[0])**2 + (player.y - pellet[1])**2 < PELLET_COLLISION_RADIUS: # Collision radius
                self.pellets.remove(pellet)
                return True
        return False
    
    
    def snap_to_grid(value):
        # Snap pixel position to nearest TILE_SIZE multiple
        return (value // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
        # e.g. if TILE_SIZE=32, and x=45, it snaps to 48 (center of tile at 32-64)


    def import_map(self, filename):
        with open(filename, "r") as f:
            for line in f:
                # remove newline characters and store each character
                self.map.append(list(line.rstrip("\n")))
