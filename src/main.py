import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Elon Musk")

# Colors
WHITE = (255, 255, 255)

# Game settings
gravity = 0.25
bird_jump = -6
bird_width, bird_height = 50, 50  # Adjusted for Elon Musk's image
pipe_width = 50
pipe_gap = 150
pipe_velocity = 4

# Fonts
font = pygame.font.SysFont("Arial", 30)

# Load images
elon_image = pygame.image.load("images/elon_closed.png")  # Use Elon Musk image
elon_image = pygame.transform.scale(elon_image, (bird_width, bird_height))  # Resize as needed
cybertruck_image = pygame.image.load("images/cybertruck.png")  # Use Cybertruck image
model_s_image = pygame.image.load("images/model_s.png")  # Use Model S image

# Bird class
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0
        self.image = elon_image

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
        self.top_height = self.height  # Height of the top pipe
        self.bottom_height = HEIGHT - self.height - pipe_gap  # Height of the bottom pipe

        # Stretch the images to fill the pipe height
        self.top_image = pygame.transform.scale(cybertruck_image, (pipe_width, self.top_height))
        self.bottom_image = pygame.transform.scale(model_s_image, (pipe_width, self.bottom_height))

    def update(self):
        self.x -= pipe_velocity

    def draw(self, screen):
        # Draw the top pipe (Cybertruck image)
        screen.blit(self.top_image, (self.x, 0))

        # Draw the bottom pipe (Model S image)
        screen.blit(self.bottom_image, (self.x, self.height + pipe_gap))

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
            score_text = font.render(f"Score: {score}", True, (0, 0, 0))
            screen.blit(score_text, (10, 10))

        # Draw Game Over screen
        if game_over:
            game_over_text = font.render("Game Over!", True, (0, 0, 0))
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
            restart_text = font.render("Press R to Restart", True, (0, 0, 0))
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 40))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_loop()  # Restart the game

        pygame.display.update()

# Run the game loop
game_loop()

# Quit Pygame
pygame.quit()
