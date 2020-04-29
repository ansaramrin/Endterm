import pygame
from enum import Enum
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Times new roman', 32)
screen = pygame.display.set_mode((800, 600))



tank_fire_sound = pygame.mixer.Sound('shooting.wav')
tank_hit_sound = pygame.mixer.Sound('hit.wav')


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


bullet = []


class Tank:

    def __init__(self, x, y, speed, color, attack, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP, d_down=pygame.K_DOWN):
        self.x = x
        self.y = y
        self.attack = attack
        self.hp = 3
        self.speed = speed
        self.color = color
        self.width = 40
        self.time = 100
        self.direction = Direction.RIGHT
        self.cannonXY = [self.x + self.width +
                         int(self.width/2), self.y + int(self.width/2)]
        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT,
                    d_up: Direction.UP, d_down: Direction.DOWN}

    def draw(self):
        tank_c = (self.x + int(self.width / 2), self.y + int(self.width / 2))
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width / 2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width +
                                                          int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (self.x -
                                                          int(self.width / 2), self.y + int(self.width / 2)), 4)

        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x +
                                                          int(self.width / 2), self.y - int(self.width / 2)), 4)

        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x +
                                                          int(self.width / 2), self.y + self.width + int(self.width / 2)), 4)

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
            self.cannonXY = [
                self.x - int(self.width / 2), self.y + int(self.width / 2)]
        if self.direction == Direction.RIGHT:
            self.x += self.speed
            self.cannonXY = [self.x + self.width +
                             int(self.width / 2), self.y + int(self.width / 2)]
        if self.direction == Direction.UP:
            self.y -= self.speed
            self.cannonXY = [
                self.x + int(self.width / 2), self.y - int(self.width / 2)]
        if self.direction == Direction.DOWN:
            self.y += self.speed
            self.cannonXY = [
                self.x + int(self.width / 2), self.y + self.width + int(self.width / 2)]
        self.draw()

    def fire(self):
        bullet.append(Bullet(self.cannonXY, self.direction,
                             self.color, self, self.time))


class Bullet():
    def __init__(self, cannonXY, direction, color, tank, time):
        self.cannonXY = cannonXY
        self.direction = direction
        self.color = color
        self.speed = 4
        self.tank = tank
        self.time = time

    def move(self):
        if self.direction == Direction.RIGHT:
            self.cannonXY[0] += self.speed
        if self.direction == Direction.LEFT:
            self.cannonXY[0] -= self.speed
        if self.direction == Direction.UP:
            self.cannonXY[1] -= self.speed
        if self.direction == Direction.DOWN:
            self.cannonXY[1] += self.speed
        pygame.draw.circle(screen, self.color, self.cannonXY, 2)
        self.time -= 1


mainloop = True
tank1 = Tank(300, 300, 2, (255, 123, 100), pygame.K_RETURN)
tank2 = Tank(100, 200, 2, (100, 230, 40), pygame.K_SPACE,
             pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)

tanks = [tank1, tank2]
FPS = 40
clock = pygame.time.Clock()

while mainloop:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False

            for tank in tanks:
                if event.key in tank.KEY.keys():

                    tank.change_direction(tank.KEY[event.key])
                if event.key == tank.attack:
                    pygame.mixer.Sound.play(tank_fire_sound)
                    tank.fire()
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (50, 100, 700, 480), 5)

    for tank in tanks:
        if tank.x + tank.width + tank.speed >= 750:
            tank.x = 50
        if tank.y + tank.width + tank.speed >= 580:
            tank.y = 100
        if tank.x + tank.speed <= 50:
            tank.x = 750 - tank.width - tank.speed
        if tank.y + tank.speed <= 100:
            tank.y = 580 - tank.width - tank.speed

    for bullets in range(len(bullet)):
        if bullet[bullets].cannonXY[0] + bullet[bullets].speed >= 750:
            bullet[bullets].cannonXY[0] = 50
        if bullet[bullets].cannonXY[1] + bullet[bullets].speed >= 580:
            bullet[bullets].cannonXY[1] = 100
        if bullet[bullets].cannonXY[0] <= 50:
            bullet[bullets].cannonXY[0] = 750 - bullet[bullets].speed
        if bullet[bullets].cannonXY[1] <= 100:
            bullet[bullets].cannonXY[1] = 580 - bullet[bullets].speed

    for tank in tanks:
        if tank.hp > 0:
            tank.move()
        else:
            tank.speed = 0

    try:
        for bullets in range(len(bullet)):
            bullet[bullets].move()
            for tank in tanks:
                if ((bullet[bullets].cannonXY[0] > tank.x) and (bullet[bullets].cannonXY[0] < tank.x + tank.width) and (bullet[bullets].cannonXY[1] > tank.y) and (bullet[bullets].cannonXY[1] < tank.y + tank.width)):
                    bullet.remove(bullet[bullets])
                    tank.hp -= 1
                    pygame.mixer.Sound.play(tank_hit_sound)
            if bullet[bullets].time == 0:
                bullet.remove(bullet[bullets])
    except IndexError:
        print('', end='')

    text_1 = font.render('P l a y e r 1', True, (100, 230, 40))
    text_2 = font.render('P l a y e r 2', True, (255, 123, 100))
    text_1_1 = font.render('H P :' + str(tank2.hp), True, (100, 230, 40))
    text_2_2 = font.render('H P :' + str(tank1.hp), True, (255, 123, 100))

    screen.blit(text_1_1, (150, 40))
    screen.blit(text_2_2, (500, 40))
    screen.blit(text_1, (150, 5))
    screen.blit(text_2, (500, 5))

    if tank1.hp <= 0:
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
        font = pygame.font.SysFont('Times new roman', 64)
        text_3 = font.render('W I N', True, (255, 255, 0))
        text_2 = font.render('P l a y e r 1', True, (100, 230, 40))
        screen.blit(text_2, (250, 200))
        screen.blit(text_3, (300, 280))


    if tank2.hp <= 0:
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 600))
        font = pygame.font.SysFont('Times new roman', 64)
        text_3 = font.render('W I N', True, (255, 255, 0))
        text_2 = font.render('P l a y e r 2', True, (255, 123, 100))
        screen.blit(text_2, (250, 200))
        screen.blit(text_3, (300, 280))


    pygame.display.flip()
pygame.quit()