import pygame 
import sys



# general setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# main window
screen_width = 1280
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')

# recs
player = pygame.Rect(screen_width / 2 - 15, screen_height - 50, 30, 30)
ball = pygame.Rect(player.left - 15, player.top - 15, 30, 30)

bg_color = pygame.Color('yellow')

# main loop
while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)



    pygame.display.flip()