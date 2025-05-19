import pygame
import sys
import random

pygame.init()

window_width = 700
window_height = 500
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Snake Game")

snake_color = (216, 191, 216)
snake_size = 18
snake_speed = 5
snake_speed_multiplier = 1

snake_x = window_width // 2
snake_y = window_height // 2

snake_dx = 0
snake_dy = 0
snake = pygame.Rect(snake_x, snake_y, snake_size, snake_size)
snake_body = []

food_color = (0, 191, 255)
food_size = 10
food_x = random.randint(0, window_width - food_size)
food_y = random.randint(0, window_height - food_size)
food = pygame.Rect(food_x, food_y, food_size, food_size)

score = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_dx = -1
        snake_dy = 0
    elif keys[pygame.K_RIGHT]:
        snake_dx = 1
        snake_dy = 0
    elif keys[pygame.K_UP]:
        snake_dx = 0
        snake_dy = -1
    elif keys[pygame.K_DOWN]:
        snake_dx = 0
        snake_dy = 1

    snake.x += snake_dx * snake_speed * snake_speed_multiplier
    snake.y += snake_dy * snake_speed * snake_speed_multiplier

    if snake.x < 0 or snake.x + snake_size > window_width or snake.y < 0 or snake.y + snake_size > window_height:
        running = False

    if snake.colliderect(food):
        snake_size += 1
        score += 1
        food.x = random.randint(0, window_width - food_size)
        food.y = random.randint(0, window_height - food_size)

    snake_body.append(pygame.Rect(snake.x, snake.y, snake_size, snake_size))
    if len(snake_body) > snake_size:
        del snake_body[0]
    for i in range(1, len(snake_body)):
        if snake.colliderect(snake_body[i]):
            running: False

    game_window.fill((0, 0, 0))
    pygame.draw.rect(game_window, snake_color, snake)
    for body_part in snake_body:
        pygame.draw.rect(game_window, snake_color, body_part)
    pygame.draw.rect(game_window, food_color, food)

    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render("Final Score: " + str(score), True, (255, 255, 255))
    game_window.blit(score_text, (10, 10))

    if score > 0 and score % 5 == 0:
        snake_speed_multiplier += 0.1

    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()

