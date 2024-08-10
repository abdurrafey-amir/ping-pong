import pygame
import sys
import random

# Functions
def player_ani():
    global player_speed
    player.x += player_speed
    if player.right >= screen_width:
        player.right = screen_width
    if player.left <= 0:
        player.left = 0

def ball_ani():
    global ball_speed_x, ball_speed_y, player, score, game_over
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1
    if ball.left <= 0:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1
    if ball.top <= 0:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    if ball.colliderect(player):
        pygame.mixer.Sound.play(pong_sound)
        if ball_speed_x > 0:
            if abs(ball.right - player.left) < 10:
                ball_speed_x *= -1
                score += 1
            elif abs(ball.left - player.right) < 10:
                ball_speed_x *= -1
                score += 1
        if ball_speed_y > 0:
            if abs(ball.bottom - player.top) < 10:
                ball_speed_y *= -1
                score += 1
            elif abs(ball.top - player.bottom) < 10:
                ball_speed_y *= -1
                score += 1
    if ball.bottom >= screen_height:
        pygame.mixer.Sound.play(game_over_sound)
        game_over = True

# General setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Main window
screen_width = 480
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')

# Recs
player = pygame.Rect(screen_width / 2 - 40, screen_height - 30, 80, 20)
ball = pygame.Rect(screen_width / 2 - 7.5, 200, 25, 25)
player_speed = 0
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5

# Colors
bg_color = pygame.Color('yellow')
sc_color = pygame.Color('black')

# Text
score = 0
high_score = 0
font = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 15)

# Timer
game_over = False
menu = True

# Sounds
pong_sound = pygame.mixer.Sound('pong.ogg')
game_over_sound = pygame.mixer.Sound('gameover.ogg')

# Main loop
while True:
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and menu:
                menu = False
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                score = 0
                ball.center = (screen_width / 2, screen_height / 2)
            if event.key == pygame.K_RIGHT:
                player_speed += 6
            if event.key == pygame.K_LEFT:
                player_speed -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_speed -= 6
            if event.key == pygame.K_LEFT:
                player_speed += 6

    # Menu screen
    if menu:
        screen.fill(sc_color)
        text = font.render('Ping Pong', False, pygame.Color('white'))
        screen.blit(text, (screen_width / 2 - 80, screen_height / 2))
        text_2 = font2.render('press space to start', False, pygame.Color('white'))
        screen.blit(text_2, (screen_width / 2 - 80, screen_height / 2 + 40))
        pygame.display.flip()
        continue

    # Functions
    player_ani()
    ball_ani()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)

    # Text
    score_text = font.render(f'{score}', False, sc_color)
    screen.blit(score_text, (screen_width / 2 - 10, screen_height / 2))

    # Game over screen
    if game_over:
        screen.fill(sc_color)
        text = font.render('Game Over!', False, pygame.Color('white'))
        screen.blit(text, (screen_width / 2 - 80, screen_height / 2))
        text_2 = font.render(f'Score: {score}', False, pygame.Color('white'))
        screen.blit(text_2, (screen_width / 2 - 50, screen_height / 2 + 40))
        text_3 = font.render(f'High Score: {high_score}', False, pygame.Color('white'))
        screen.blit(text_3, (screen_width / 2 - 80, screen_height / 2 + 80))
        text_4 = font2.render('press space to try again', False, pygame.Color('white'))
        screen.blit(text_4, (screen_width / 2 - 80, screen_height / 2 + 120))
        if score > high_score:
            high_score = score
        pygame.display.flip()
        continue

    # Update high score
    if score > high_score:
        high_score = score

    pygame.display.flip()
    clock.tick(80)