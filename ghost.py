# ghost.py

import pygame
import random
import time
from settings import TILE_SIZE, SHOW_NAMES




class Ghost:
    def __init__(self, x, y, color, name, behaviour, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = TILE_SIZE // 2 - 2
        self.color = color
        self.name = name
        self.behaviour = behaviour
        self.font = pygame.font.SysFont("Arial", 14, bold=True)
        
        self.dx = 0
        # start moving up by default to escape prison faster
        self.dy = -self.speed 

        self.last_direction_change = time.time()
        self.change_delay = random.uniform(1, 3) # seconds
    

    def update(self, grid):
        current_time = time.time()

        # Change direction every few seconds
        if current_time - self.last_direction_change > self.change_delay:
            self.choose_direction(grid) # pass grid to avoid blocked moves
            self.last_direction_change = current_time
            self.change_delay = random.uniform(1, 3)
            # print ("Changing direction for", self.name, "to", (self.dx, self.dy))

        new_x = self.x + self.dx
        new_y = self.y + self.dy

        # If hitting a wall, force new direction
        if grid.is_wall(new_x, self.y):
            self.choose_direction(grid)
            return
        
        if grid.is_wall(self.x, new_y):
            self.choose_direction(grid)
            return
        
        self.x = new_x
        self.y = new_y



    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        if SHOW_NAMES:
            # render text name
            text_surface = self.font.render(self.name, True, self.color)
        
            # center text above ghost
            text_rect = text_surface.get_rect()
            text_rect.center = (self.x, self.y - TILE_SIZE)

            # draw
            screen.blit(text_surface, text_rect)

        
    

    def choose_direction(self, grid):
        # Only allow directions that are not blocked
        possible_directions = [
            (self.speed, 0), # right
            (-self.speed, 0), # left
            (0, self.speed), # down
            (0, -self.speed) # up
        ]

        # Filter out blocked directions (walls)
        valid_directions = []
        for dx, dy in possible_directions:
            new_x = self.x + dx
            new_y = self.y + dy
            if not grid.is_wall(new_x, new_y):
                valid_directions.append((dx, dy))

        if valid_directions:
            self.dx, self.dy = random.choice(valid_directions)
        else:
            # stuck inside a dead end: stop
            self.dx, self.dy = 0, 0
        