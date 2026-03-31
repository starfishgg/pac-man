# player.py

import pygame
from settings import TILE_SIZE, YELLOW, PLAYER_SPEED




class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED
        self.dx = 0
        self.dy = 0
        self.radius = TILE_SIZE // 2 - 2


    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dx, self.dy = -self.speed, 0
        elif keys[pygame.K_RIGHT]:
            self.dx, self.dy = self.speed, 0
        elif keys[pygame.K_UP]:
            self.dx, self.dy = 0, -self.speed
        elif keys[pygame.K_DOWN]:
            self.dx, self.dy = 0, self.speed


    def update(self, grid):
        new_x = self.x + self.dx
        new_y = self.y + self.dy

        # Check for wall collisions before moving
        if not grid.is_wall(new_x, self.y):
            self.x = new_x
        
        if not grid.is_wall(self.x, new_y):
            self.y = new_y


    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)
