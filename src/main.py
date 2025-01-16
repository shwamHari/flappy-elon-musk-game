# main.py
import pygame
from constants import *
from bird import Bird
from pipe import Pipe
from utils import load_image
from constants import FONT

# Initialize Pygame
pygame.init()

# Create the screen (Pygame window)
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set the screen dimensions
pygame.display.set_caption("Flappy Elon Musk Game")  # Set the window title

# Load images
elon_image_closed = load_image("images/elon_closed.png")
elon_image_opened = load_image("images/elon_opened.png")
cybertruck_image = load_image("images/cybertruck.png")
model_s_image = load_image("images/model_s.png")

# Create instances of Bird and Pipe
bird = Bird(elon_image_closed, elon_image_opened)
pipe_images = [cybertruck_image, model_s_image]
pipes = [Pipe(pipe_images)]


def reset_game():
    # Create a new bird with initial position and state
    bird = Bird(elon_image_closed, elon_image_opened)

    # Create a list with one pipe to start
    pipes = [Pipe(pipe_images)]

    # Reset score
    score = 0

    # Reset game over flag
    game_over = False

    return bird, pipes, score, game_over


# Game loop
def game_loop():
    # Initialize game state
    bird, pipes, score, game_over = reset_game()

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(60)
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.jump()
                elif event.key == pygame.K_r and game_over:  # Restart the game if "R" is pressed
                    bird, pipes, score, game_over = reset_game()

        if not game_over:
            # Update bird position
            bird.update()

            # Check for top and bottom screen collisions
            if bird.y <= 0 or bird.y + BIRD_HEIGHT >= HEIGHT:
                game_over = True

            # Add new pipes
            if pipes[-1].x < WIDTH - 200:
                pipes.append(Pipe(pipe_images))

            # Move pipes
            for pipe in pipes:
                pipe.update()
                if pipe.x + PIPE_WIDTH < 0:
                    pipes.remove(pipe)
                    score += 1

                # Check for collisions using masks
                if pipe.check_collision(bird):
                    game_over = True

            # Draw everything
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)

            # Draw the score
            score_text = FONT.render(f"Score: {score}", True, (0, 0, 0))
            screen.blit(score_text, (10, 10))

        # Draw Game Over screen
        if game_over:
            game_over_text = FONT.render("Game Over!", True, (0, 0, 0))
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
            restart_text = FONT.render("Press R to Restart", True, (0, 0, 0))
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 40))

        pygame.display.update()

# Run the game loop
game_loop()

# Quit Pygame
pygame.quit()
