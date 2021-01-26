import pygame

pygame.init()

win_width = 1280
win_height = 960

paddle_width = 20
paddle_height = 100
paddle_speed = 20

pong_width = 20
pong_height = 20

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('Pong')

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([paddle_width, paddle_height])
        self.image.fill(light_grey)
        self.rect = self.image.get_rect()
        self.score = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([pong_width, pong_height])
        self.image.fill(light_grey)
        self.rect = self.image.get_rect()
        self.speed = 20
        self.dx = 1
        self.dy = 1

player_paddle = Paddle()
player_paddle.rect.x = paddle_width
player_paddle.rect.y = win_height / 2

opponent_paddle = Paddle()
opponent_paddle.rect.x = win_width - (paddle_width * 2)
opponent_paddle.rect.y = win_height / 2

pong = Ball()
pong.rect.x = win_width / 2
pong.rect.y = win_height / 2

all_sprites = pygame.sprite.Group()
all_sprites.add(player_paddle, opponent_paddle, pong)

def redraw():
    win.fill(bg_color)
    all_sprites.draw(win)
    pygame.display.update()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player_paddle.rect.y += -(paddle_speed)
    if key[pygame.K_s]:
        player_paddle.rect.y += (paddle_speed)
    if key[pygame.K_UP]:
        opponent_paddle.rect.y += -(paddle_speed)
    if key[pygame.K_DOWN]:
        opponent_paddle.rect.y += (paddle_speed)
    
    pong.rect.x += pong.speed
    pong.rect.y += pong.speed

    redraw()

pygame.quit()
