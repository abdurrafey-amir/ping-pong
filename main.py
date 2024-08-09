import pygame 
import sys
import random

# functions
def player_ani():
    player.x += player_speed
    if player.right >= screen_width:
        player.right = screen_width
    if player.left <= 0:
        player.left = 0

def ball_ani():
    global ball_speed_x, ball_speed_y, player
    
    # ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.right >= screen_width:
        # ball.right = screen_width
        ball_speed_x *= -1
    if ball.left <= 0:
        # ball.left = 0
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.colliderect(player):
        ball_speed_y *= -1


# general setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()



# main window
screen_width = 1280
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')


# recs
player = pygame.Rect(screen_width / 2 - 15, screen_height - 50, 120, 30)
ball = pygame.Rect(player.left + 35, player.top - 15, 30, 30)
player_speed = 0
ball_speed_x = 1.5 * random.choice((1, -1))
ball_speed_y = 1.5 * random.choice((1, -1))

bg_color = pygame.Color('yellow')

# main loop
while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_speed += 2
            if event.key == pygame.K_LEFT:
                player_speed -= 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_speed -= 2
            if event.key == pygame.K_LEFT:
                player_speed += 2

    # functions
    player_ani()
    ball_ani()

    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)



    pygame.display.flip()