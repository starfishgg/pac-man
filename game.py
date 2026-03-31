# game.py


# TO DO:
# - Load levels from a file instead of hardcoding the map - DONE
# - Snap players and ghosts to the grid
# - Warp tunnels on the sides of the map
# - Add more complex ghost behaviours
# - Add power pellets and frightened mode
# - Add sound effects and music - DONE
# - Add a start screen and game over screen
# - Add more levels with different mazes
# - Add a high score system
# - Improve graphics/animations
# - Multiplayer mode with 2 players controlling different characters

import pygame
from settings import *
from player import Player
from ghost import Ghost
from grid import Grid



class Game:
    def __init__(self):

        self.clock = pygame.time.Clock()
        self.grid = Grid(BLUE, WHITE)

        # Calculate the center tile of the grid to place the player and ghosts
        rows = len(self.grid.map)
        cols = len(self.grid.map[0])
        center_row = rows // 2
        center_col = cols // 2
        x, y = self.get_tile_center(center_col, center_row)

        # Initialize Pygame and set up the game window
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((cols * TILE_SIZE, rows * TILE_SIZE))
        pygame.display.set_caption("Pac-Man OOP")

        # Set up font for score display
        self.font = pygame.font.SysFont("Arial", 32, bold=True)


        # Place the player slightly below the center tile to avoid immediate collision with ghosts
        self.player = Player(x, y+TILE_SIZE*2)
        self.ghosts = []

        # Add the four main ghosts with their respective colors, names, and behaviours
        self.add_ghost(x, y, RED, "Blinky", "Chaser", GHOST_SPEED)
        self.add_ghost(x-TILE_SIZE*1, y, PINK, "Pinky", "Ambusher", GHOST_SPEED)
        self.add_ghost(x-TILE_SIZE*1, y, CYAN, "Inky", "Fickle", GHOST_SPEED)
        self.add_ghost(x, y, ORANGE, "Clyde", "Random", GHOST_SPEED)

        self.score = 0
        self.running = True

        pygame.mixer.music.load(BGM_SFX)
        pygame.mixer.Sound(DEATH_SFX)
        pygame.mixer.Sound(EAT_PELLET_SFX)
        pygame.mixer.music.play(-1) # loop indefinitely



    def add_ghost(self, x, y, color, name, behaviour, speed=GHOST_SPEED):
        ghost = Ghost(x, y, color, name, behaviour, speed)
        self.ghosts.append(ghost)
        return True



    def check_collision(self):
        for ghost in self.ghosts:
            dx = self.player.x - ghost.x
            dy = self.player.y - ghost.y
            if dx*dx + dy*dy < GHOST_COLLISION_RADIUS:
                return True
        return False



    def run(self):
        while self.running:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            #####################
            # Handle player INPUT
            #####################

            self.player.handle_input()


            ###################
            # Update GAME STATE
            ###################

            self.player.update(self.grid)

            for ghost in self.ghosts:
                ghost.update(self.grid)


            ######################
            # Check for COLLISIONS
            ######################

            if self.grid.check_collision(self.player):
                self.score += 1 * PELLET_SCORE
                pygame.mixer.Sound(EAT_PELLET_SFX).play()

            if self.check_collision():
#                print("Game Over! Final Score:", self.score)
                pygame.mixer.Sound(DEATH_SFX).play()
                self.running = False


            #################
            # Draw EVERYTHING
            #################

            self.screen.fill(BLACK)

            self.grid.draw(self.screen)
            self.player.draw(self.screen)
            for ghost in self.ghosts:
                ghost.draw(self.screen)

            self.draw_score()

            pygame.display.flip()
    
        pygame.mixer.music.stop()
        pygame.time.wait(2000) # wait 2 seconds before closing to finish SFX
        print("Game Over! Final Score:", self.score)
        pygame.quit()


    def get_tile_center(self, col, row):
        x = col * TILE_SIZE + TILE_SIZE // 2
        y = row * TILE_SIZE + TILE_SIZE // 2
        return x, y
    

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, YELLOW)
        text_rect = score_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + TILE_SIZE * SCORE_OFFSET))
        self.screen.blit(score_text, text_rect)
