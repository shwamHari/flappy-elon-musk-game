import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone with a Twist")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game settings
gravity = 0.25
bird_jump = -6
bird_width, bird_height = 30, 30
pipe_width = 50
pipe_gap = 150
pipe_velocity = 4

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Bird class
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0
        self.image = pygame.Surface((bird_width, bird_height))
        self.image.fill(BLUE)

    def update(self):
        self.velocity += gravity
        self.y += self.velocity

    def jump(self):
        self.velocity = bird_jump

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT - pipe_gap - 100)
        self.top = pygame.Rect(self.x, 0, pipe_width, self.height)
        self.bottom = pygame.Rect(self.x, self.height + pipe_gap, pipe_width, HEIGHT - self.height - pipe_gap)

    def update(self):
        self.x -= pipe_velocity
        self.top.x = self.x
        self.bottom.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.top)
        pygame.draw.rect(screen, GREEN, self.bottom)

# Game loop
def game_loop():
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()
    score = 0
    running = True
    game_over = False

    while running:
        clock.tick(60)
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        if not game_over:
            # Update bird position
            bird.update()

            # Add new pipes
            if pipes[-1].x < WIDTH - 200:
                pipes.append(Pipe())

            # Move pipes
            for pipe in pipes:
                pipe.update()
                if pipe.x + pipe_width < 0:
                    pipes.remove(pipe)
                    score += 1

                # Check for collisions
                if bird.x + bird_width > pipe.x and bird.x < pipe.x + pipe_width:
                    if bird.y < pipe.height or bird.y + bird_height > pipe.height + pipe_gap:
                        game_over = True

            # Draw everything
            bird.draw(screen)
            for pipe in pipes:
                pipe.draw(screen)

            # Draw the score
            score_text = font.render(f"Score: {score}", True, BLACK)
            screen.blit(score_text, (10, 10))

        # Draw Game Over screen
        if game_over:
            game_over_text = font.render("Game Over!", True, BLACK)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
            restart_text = font.render("Press R to Restart", True, BLACK)
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 40))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_loop()  # Restart the game

        pygame.display.update()

# Run the game loop
game_loop()

# Quit Pygame
pygame.quit()






