import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (213, 50, 80)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()
speed = 15

# Font settings
font = pygame.font.SysFont("bahnschrift", 25)

# Function to display score
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

# Function to draw the snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position
    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0

    # Snake body
    snake_body = []
    length_of_snake = 1

    # Food position
    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            msg = font.render("Game Over! Press C-Continue or Q-Quit", True, RED)
            screen.blit(msg, [WIDTH // 6, HEIGHT // 3])
            show_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = BLOCK_SIZE

        # Move snake
        x += x_change
        y += y_change

        # Check collision with boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Update screen
        screen.fill(BLACK)

        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        # Update snake
        snake_head = [x, y]
        snake_body.append(snake_head)

        if len(snake_body) > length_of_snake:
            del snake_body[0]

        # Check collision with itself
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_body)
        show_score(length_of_snake - 1)

        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            length_of_snake += 1

        # Control speed
        clock.tick(speed)

    pygame.quit()
    quit()

# Run the game
game_loop()
