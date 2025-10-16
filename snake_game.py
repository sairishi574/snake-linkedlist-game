# snake_game.py
# ---------------------------------------
# Snake Game using Linked List and pygame

import pygame
import sys
import random
from snake_linkedlist import LinkedList

# Initialize pygame
pygame.init()
pygame.display.set_caption("Snake Game using Linked List")

# Game setup
cell_size = 20
cols, rows = 30, 20
screen = pygame.display.set_mode((cols * cell_size, rows * cell_size))
clock = pygame.time.Clock()

# Snake setup (Linked List)
snake = LinkedList()
snake.insert_at_beginning(10, 10)
direction = (1, 0)  # Start moving right
food = (random.randint(0, cols - 1), random.randint(0, rows - 1))
score = 0

# Draw game objects
def draw():
    screen.fill((0, 0, 0))

    # Draw food
    pygame.draw.rect(screen, (255, 0, 0), (food[0]*cell_size, food[1]*cell_size, cell_size, cell_size))

    # Draw snake
    for x, y in snake.get_positions():
        pygame.draw.rect(screen, (0, 255, 0), (x * cell_size, y * cell_size, cell_size, cell_size))

    # Display score
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.update()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    if keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    if keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    if keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    # Move snake head
    head_x, head_y = snake.head.x + direction[0], snake.head.y + direction[1]
    snake.insert_at_beginning(head_x, head_y)

    # Food eating condition
    if (head_x, head_y) == food:
        food = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        score += 1
    else:
        snake.delete_at_end()

    # Collision conditions
    positions = snake.get_positions()
    if (head_x < 0 or head_y < 0 or head_x >= cols or head_y >= rows or (head_x, head_y) in positions[1:]):
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    draw()
    clock.tick(10)  # Speed of the snake
