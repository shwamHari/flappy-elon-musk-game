# main.py
import pygame
from constants import *
from bird import Bird
from pipe import Pipe
from utils import load_image

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

# Font setup
FONT = pygame.font.SysFont("Arial", 30)

# Function to display the welcome screen
def welcome_screen(screen, font):
    """
    Displays the welcome screen with a slower animated title and Elon jumping animation.
    """
    running = True

    # Title animation variables
    title_y = HEIGHT // 3
    title_direction = 1  # 1 = moving down, -1 = moving up
    title_speed = 0.2  # Slower speed of vertical movement
    color_index = 0  # To cycle through colors
    color_change_timer = 0  # Timer for slowing down color changes
    colors = [(255, 255, 255), (200, 200, 255), (255, 200, 200)]  # Color cycle

    # Resize Elon images to 50x50 pixels
    elon_image_closed_scaled = pygame.transform.scale(elon_image_closed, (50, 50))
    elon_image_opened_scaled = pygame.transform.scale(elon_image_opened, (50, 50))

    # Elon jumping animation variables
    elon_y = HEIGHT // 2  # Center Y position for Elon
    elon_direction = -1  # -1 = jumping up, 1 = falling down
    elon_speed = 0.5  # Slower jump speed

    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))  # Black background

        # Animate the title's vertical position slowly
        title_y += title_direction * title_speed
        if title_y > HEIGHT // 3 + 20 or title_y < HEIGHT // 3 - 20:
            title_direction *= -1  # Reverse direction

        # Slow down the color cycling using a timer
        color_change_timer += 1
        if color_change_timer > 20:  # Change color every 20 frames
            color_index = (color_index + 1) % len(colors)
            color_change_timer = 0

        # Render the title text
        title_text = font.render("Welcome To Flappy Elon", True, colors[color_index])
        title_rect = title_text.get_rect(center=(WIDTH // 2, round(title_y)))
        screen.blit(title_text, title_rect)

        # Instructions text
        instructions_text = font.render("Press SPACE to Start", True, (200, 200, 200))
        instructions_rect = instructions_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(instructions_text, instructions_rect)

        # Update Elon's Y position
        elon_y += elon_direction * elon_speed

        # Switch direction and update image based on movement
        if elon_y <= HEIGHT // 2 - 50:  # Top of the jump
            elon_direction = 1  # Start falling down
        elif elon_y >= HEIGHT // 2:  # Bottom of the jump
            elon_direction = -1  # Start jumping up

        # Set image based on direction
        elon_image = elon_image_opened_scaled if elon_direction == -1 else elon_image_closed_scaled

        # Draw Elon
        screen.blit(elon_image, (WIDTH // 2 - 25, int(elon_y)))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False

        # Update the screen and set frame rate
        pygame.display.flip()
        clock.tick(200)  # Limit to 60 frames per second


# Function to reset the game state
def reset_game():
    bird = Bird(elon_image_closed, elon_image_opened)
    pipes = [Pipe([cybertruck_image, model_s_image])]
    score = 0
    game_over = False
    return bird, pipes, score, game_over


# Game loop function
def game_loop():
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
                elif event.key == pygame.K_r and game_over:
                    bird, pipes, score, game_over = reset_game()

        if not game_over:
            bird.update()

            # Check for collisions with the screen edges
            if bird.y <= 0 or bird.y + BIRD_HEIGHT >= HEIGHT:
                game_over = True

            # Manage pipes
            if pipes[-1].x < WIDTH - 200:
                pipes.append(Pipe([cybertruck_image, model_s_image]))
            for pipe in pipes:
                pipe.update()
                if pipe.x + PIPE_WIDTH < 0:
                    pipes.remove(pipe)
                    score += 1
                if pipe.check_collision(bird):
                    game_over = True

            # Draw objects
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)

            # Display score
            score_text = FONT.render(f"Score: {score}", True, (0, 0, 0))
            screen.blit(score_text, (10, 10))

        else:
            # Game Over screen
            game_over_text = FONT.render("Game Over!", True, (0, 0, 0))
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
            restart_text = FONT.render("Press R to Restart", True, (0, 0, 0))
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 40))

        pygame.display.update()

    pygame.quit()


# Run the game with a welcome screen
welcome_screen(screen, FONT)
game_loop()
