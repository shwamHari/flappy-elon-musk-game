# pipe.py
import pygame
import random
from constants import PIPE_WIDTH, PIPE_GAP, PIPE_VELOCITY, HEIGHT, WIDTH

class Pipe:
    def __init__(self, images):
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT - PIPE_GAP - 100)
        self.top_height = self.height
        self.bottom_height = HEIGHT - self.height - PIPE_GAP

        self.top_image = pygame.transform.scale(images[0], (PIPE_WIDTH, self.top_height))
        self.bottom_image = pygame.transform.scale(images[1], (PIPE_WIDTH, self.bottom_height))

        self.top_mask = pygame.mask.from_surface(self.top_image)
        self.bottom_mask = pygame.mask.from_surface(self.bottom_image)

    def update(self):
        self.x -= PIPE_VELOCITY

    def draw(self, screen):
        screen.blit(self.top_image, (self.x, 0))
        screen.blit(self.bottom_image, (self.x, self.height + PIPE_GAP))

    def get_top_rect(self):
        return pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)

    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, self.bottom_height)

    def check_collision(self, bird):
        top_rect = self.get_top_rect()
        bottom_rect = self.get_bottom_rect()

        if top_rect.colliderect(bird.get_rect()):
            offset = (self.x - bird.x, 0)
            if self.top_mask.overlap(bird.mask, offset):
                return True

        if bottom_rect.colliderect(bird.get_rect()):
            offset = (self.x - bird.x, self.height + PIPE_GAP - bird.y)
            if self.bottom_mask.overlap(bird.mask, offset):
                return True

        return False
