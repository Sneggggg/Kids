import random
import pygame

# Tek=os.path.dirname(__file__)
# image_folder=os.path.join(Tek,'Game_god')
# #plimage=pygame.image.load(os.path.join(image_folder,'Ёлка1.png')).convert()


width = 600  # Окно игры
height = 800
Black = (150, 255, 234)

FPS = 60

class Player(pygame.sprite.Sprite):  # Игрок
    def __init__(self):  # Инициализация игрока
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((30, 30))  # Размер прямоуголника
        self.image.fill((255, 145, 3))  # Цвет прямоуголника

        self.rect = self.image.get_rect()  # Создание прямоуголника
        self.rect.center = (width / 2, height / 2)  # Центр прямоуголника

    def bulletts(self):
        bul = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bul)
        bullet.add(bul)

    def update(self):

        self.speedX = 0
        self.speedY = 0

        key_tracking = pygame.key.get_pressed()  # Словар совсеми клавишоми

        if key_tracking[pygame.K_LEFT]:
            self.speedX = -8

        if key_tracking[pygame.K_RIGHT]:
            self.speedX = 8

        if key_tracking[pygame.K_UP]:
            self.speedY = -8

        if key_tracking[pygame.K_DOWN]:
            self.speedY = 8

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        # блок запрета движения
        if self.rect.right > width:
            self.rect.right = width

        if self.rect.left < 0:
            self.rect.left = 0


class Enemy(pygame.sprite.Sprite):  # врага
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((50, 50))  # Размер врага (форма не определена)
        self.image.fill((255, 54, 41))  # Цвет врага

        self.rect = self.image.get_rect()  # Создание врага по форме прямоугольника
        # self.rect.center = (width / 3, height / 3)  # Центр врага
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(4, 15)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
            self.rect.x = random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 5))
        self.image.fill((250, 145, 3))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.center = x
        self.speedy = -5

    def uppdate(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

pygame.init()  # Запуск игры
pygame.mixer.init()  # Звук
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Игра Бога")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()  # Добовление спрайта в групу
enemy = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

bullet = pygame.sprite.Group()

all_sprites.add(bullet)

for i in range(1):  # спавн мабов
    mob = Enemy()
    all_sprites.add(mob)
    enemy.add(mob)

run = True
while run:

    clock.tick(FPS)  # Ограничения FPS

    for event in pygame.event.get():  # Выход на крестик
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.bulletts()

    collision = pygame.sprite.groupcollide(enemy,bullet
                                           ,True,True)
    for i in collision:
        mob = Enemy()
        all_sprites.add(mob)
        enemy.add(mob)

    all_sprites.update()
    collision = pygame.sprite.spritecollide(player, enemy, False)
    if collision:
        run = False
    screen.fill(Black)  # Заливка0
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
