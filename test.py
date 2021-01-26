import pygame, sys, random

def ball_animation():

    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= scrn_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= scrn_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= scrn_height:
        player.bottom = scrn_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.top > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= scrn_height:
        opponent.bottom = scrn_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (scrn_width / 2, scrn_height / 2)
    ball_speed_y *= random.choice((-1, 1))
    ball_speed_x *= random.choice((-1, 1))

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window

scrn = pygame.display.set_mode((scrn_width, scrn_height))
pygame.display.set_caption('Pong')

# Game rectangles
ball = pygame.Rect(scrn_width / 2 - 15, scrn_height / 2 - 15, 30, 30)
player = pygame.Rect(scrn_width - 20, scrn_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, scrn_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 6 * random.choice((-1, 1))
ball_speed_y = 6 * random.choice((-1, 1))

player_speed = 0
opponent_speed = 7

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_DOWN:
                player_speed += 7


    ball_animation()
    player_animation()

    opponent_ai()

    # Visuals
    scrn.fill(bg_color)
    pygame.draw.rect(scrn, light_grey, player)
    pygame.draw.rect(scrn, light_grey, opponent)
    pygame.draw.ellipse(scrn, light_grey, ball)
    pygame.draw.aaline(scrn, light_grey, (scrn_width / 2, 0), (scrn_width / 2, scrn_height))
    
    # Updating the window
    pygame.display.flip()
    clock.tick(60)