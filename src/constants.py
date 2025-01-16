# constants.py

import pygame

# Initialize Pygame and font system
pygame.init()
pygame.font.init()  # Initialize the font system

WIDTH, HEIGHT = 450, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAVITY = 0.25
BIRD_JUMP = -6
BIRD_WIDTH, BIRD_HEIGHT = 50, 50
PIPE_WIDTH = 50
PIPE_GAP = int(150 * (WIDTH / 450))  # Adjusting pipe gap proportionally
PIPE_VELOCITY = 4
GRAVITY = 0.25

# Fonts
FONT_NAME = "Arial"
FONT_SIZE = 30

# Font settings
FONT = pygame.font.SysFont("Arial", 30)
