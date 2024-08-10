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
    global ball_speed_x, ball_speed_y, player, score, game_over
    
    # ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.right >= screen_width:
        # ball.right = screen_width
        # ball_speed_y *= -1
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1
    if ball.left <= 0:
        # ball.left = 0
        # ball_speed_y *= -1
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






# general setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()



# main window
screen_width = 480
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')


# recs
player = pygame.Rect(screen_width / 2 - 40, screen_height - 30, 80, 20)
ball = pygame.Rect(screen_width / 2 - 7.5, 200, 25, 25)
player_speed = 0
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5

bg_color = pygame.Color('yellow')
sc_color = pygame.Color('black')

# text
score = 0
font = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 15)

# timer
game_over = False

# sounds
pong_sound = pygame.mixer.Sound('pong.ogg')
game_over_sound = pygame.mixer.Sound('gameover.ogg')

# main loop
while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_speed += 6
            if event.key == pygame.K_LEFT:
                player_speed -= 6
            if game_over:
                if event.key == pygame.K_SPACE:
                    game_over = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_speed -= 6
            if event.key == pygame.K_LEFT:
                player_speed += 6

    # functions
    player_ani()
    ball_ani()
    

    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)

    # text
    score_text = font.render(f'{score}', False, sc_color)
    screen.blit(score_text, (screen_width / 2 - 10, screen_height / 2))

    if game_over:
        screen.fill(sc_color)
        text = font.render('Game Over!', False, pygame.Color('white'))
        screen.blit(text, (screen_width / 2 - 80, screen_height / 2))
        text_2 = font.render(f'Score: {score}', False, pygame.Color('white'))
        screen.blit(text_2, (screen_width / 2 - 50, screen_height / 2 + 40)) 
        text_3 = font2.render('press space to try again', False, pygame.Color('white'))
        screen.blit(text_3, (screen_width / 2 - 80, screen_height / 2 + 80))
        ball.center = (screen_width / 2, screen_height / 2)
    pygame.display.flip()
    clock.tick(80)