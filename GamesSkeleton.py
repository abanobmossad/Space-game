import pygame
import random

WIDTH = 400
HEIGHT = 500
FPS = 60
MOVE = 3
ENEMY_NUMS = 8

# Colors
WHITE = (255, 255, 255) 
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# initiate the game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# load images
PLAYER = "game_images/ship.png"
ENEMY = "game_images/enemy.png"
LASER = "game_images/laser.png"
BG = "game_images/bg.png"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ship
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - 10)
        self.speedx = 5
        self.speedy = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx -= 5
        elif keystate[pygame.K_RIGHT]:
            self.speedx += 5
        if self.rect.x >= WIDTH - 30:
            self.speedx -= 5
        elif self.rect.x < 2:
            self.speedx += 5
        self.rect.x = self.speedx
        print(self.rect.left)

    def shoot(self):
        b = bullets(player)
        bullets_group.add(b)
        all_sprites.add(b)


class Enemies(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemys
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, 0)
        self.espeed_y = random.randrange(1, 8)
        self.espeed_x = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.espeed_y
        self.rect.x += self.espeed_x
        if self.rect.y > HEIGHT + 10 or self.rect.x < -10 or self.rect.x > WIDTH:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, 0)
            self.espeed_y = random.randrange(1, 8)


class bullets(pygame.sprite.Sprite):
    def __init__(self, player_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.bspeed = 5
        self.rect.centerx = player_pos.rect.centerx
        self.rect.bottom = player_pos.rect.top

    def update(self):
        self.rect.y -= self.bspeed


# load images
background = pygame.image.load(BG).convert()
background_rect = background.get_rect()
ship = pygame.transform.scale(pygame.image.load(PLAYER).convert(), (50, 38))
laser = pygame.transform.scale(pygame.image.load(LASER).convert(), (10, 40))
enemys = pygame.transform.scale(pygame.image.load(ENEMY).convert(), (50, 38))

# sprites
all_sprites = pygame.sprite.Group()
mop_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
player = Player()
for i in range(ENEMY_NUMS):
    m = Enemies()
    all_sprites.add(m)
    mop_group.add(m)

all_sprites.add(player)
# Game loop
running = True

while running:
    clock.tick(FPS)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update
    all_sprites.update()

    # if bullets hit enemy
    hits = pygame.sprite.groupcollide(bullets_group, mop_group, True, True)
    for hit in hits:
        m = Enemies()
        all_sprites.add(m)
        mop_group.add(m)
    # if enemy hit player
    hit = pygame.sprite.spritecollide(player, mop_group, False)
    if hit:
        running = False
    # Draw
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # After Drawing every thing
    pygame.display.flip()

pygame.quit()
