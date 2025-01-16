import pygame
from constants import BIRD_WIDTH, BIRD_HEIGHT, BIRD_JUMP, GRAVITY  # Import constants

class Bird:
    def __init__(self, image_closed, image_opened):
        self.x = 100  # Starting X position
        self.y = 300  # Starting Y position
        self.velocity = 0  # Starting velocity

        # Resize images to the desired size from constants
        self.image_closed = pygame.transform.scale(image_closed, (BIRD_WIDTH, BIRD_HEIGHT))
        self.image_opened = pygame.transform.scale(image_opened, (BIRD_WIDTH, BIRD_HEIGHT))

        # Set the initial image
        self.image = self.image_closed
        self.mask = pygame.mask.from_surface(self.image)  # Mask for collision detection

        self.jumping_timer = 0  # Timer for jump animation

    def update(self):
        self.velocity += GRAVITY  # Gravity effect
        self.y += self.velocity  # Update the bird's position

        if self.jumping_timer > 0:
            self.jumping_timer -= 1
            self.image = self.image_opened  # Show open mouth when jumping
        else:
            self.image = self.image_closed  # Return to closed mouth when not jumping

    def jump(self):
        self.velocity = BIRD_JUMP  # Jump velocity from constants
        self.jumping_timer = 10  # Set jump timer to show the open mouth for a brief period

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Draw the bird's image on the screen

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())  # Get the bird's rectangle for collision
