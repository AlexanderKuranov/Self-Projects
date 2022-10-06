"""Игра 'Перебеги дорогу' """

import pygame
import random

pygame.init()
size = width, height = (400, 400)  #параметры окна игры 
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("comicsansms", 32)
follow = font.render("Вы победили!", 1, (255, 0, 0), (0, 255, 0))


def player(xp, yp):
    """функия отрисовки игрока"""
    pygame.draw.circle(screen, ("brown"), (xp, yp), 10)


def auto_b(x):
    """функции отписовки машин"""
    pygame.draw.rect(screen, ("blue"), (x, 65, 30, 30), 0)


def auto_r(x):
    pygame.draw.rect(screen, ("red"), (x, 112, 30, 25), 0)


def auto_y(x):
    pygame.draw.rect(screen, ("yellow"), (x, 159, 30, 20), 0)


def auto_p(x):
    pygame.draw.rect(screen, ("pink"), (x, 219, 30, 20), 0)


def auto_g(x):
    pygame.draw.rect(screen, ("green"), (x, 266, 30, 23), 0)


def auto_o(x):
    pygame.draw.rect(screen, ("orange"), (x, 313, 30, 22), 0)


def draw():
    """функция отрисовки поля"""
    screen.fill((0, 255, 0,))
    x = 3
    pygame.draw.rect(screen, pygame.Color('gray'), (0, 50, 400, 300), 0)

    pygame.draw.line(screen, pygame.Color('white'), (0, 55), (400, 55), 2)
    pygame.draw.line(screen, pygame.Color('white'), (0, 196), (400, 196), 3)
    pygame.draw.line(screen, pygame.Color('white'), (0, 204), (400, 204), 3)
    pygame.draw.line(screen, pygame.Color('white'), (0, 345), (400, 345), 2)

    for i in range(20):
        if i % 2 == 0:
            pygame.draw.line(screen, pygame.Color('white'), (x, 102), (x + 30, 102), 2)
            pygame.draw.line(screen, pygame.Color('white'), (x, 149), (x + 30, 149), 2)
            pygame.draw.line(screen, pygame.Color('white'), (x, 251), (x + 30, 251), 2)
            pygame.draw.line(screen, pygame.Color('white'), (x, 298), (x + 30, 298), 2)
        x = x + 20

"""позиционирование игрока и машин на поле"""
pos_x = 0
pos_xr = 400
pos_xy = 0
pos_xo = 400
pos_xg = 0
pos_xp = 400
xp = 200
yp = 380
speed_blue = random.randint(15, 20)
speed_red = random.randint(15, 20)
speed_yellow = random.randint(15, 20)
speed_orange = random.randint(15, 20)
speed_green = random.randint(20, 25)
speed_pink = random.randint(25, 30)
running = True
while running:
    """Цикл управление игроком"""
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            yp = yp + 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            yp = yp - 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            xp = xp + 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            xp = xp - 10
        if event.type == pygame.QUIT:
            running = False
    draw()
    auto_b(pos_x)
    auto_r(pos_xr)
    auto_y(pos_xy)
    auto_o(pos_xo)
    auto_g(pos_xg)
    auto_p(pos_xp)
    player(xp, yp)

    pos_x = pos_x + 1 + fps / speed_blue
    pos_xr = pos_xr - 1 - (fps / speed_red)
    pos_xy = pos_xy + 1 + fps / speed_yellow
    pos_xo = pos_xo - 1 - (fps / speed_orange)
    pos_xg = pos_xg + 1 + fps / speed_green
    pos_xp = pos_xp - 1 - (fps / speed_pink)
    """Условия переноса машины на исходную позицию в случае достижения конца поля"""
    if pos_xr < 0:
        pos_xr = 400
        speed_red = random.randint(10, 15)
    if pos_x > 400:
        pos_x = 0
        speed_blue = random.randint(10, 15)
    if pos_xy > 400:
        pos_xy = 0
        speed_yellow = random.randint(10, 15)
    if pos_xo < 0:
        pos_xo = 400
        speed_orange = random.randint(15, 20)
    if pos_xg > 400:
        pos_xg = 0
        speed_green = random.randint(20, 25)
    if pos_xp < 0:
        pos_xp = 400
        speed_pink = random.randint(25, 30)

    if (305 < yp < 350) and (pos_xo - 10 < xp < pos_xo + 40):
        xp = 200
        yp = 380
    if (250 < yp < 300) and (pos_xg - 10 < xp < pos_xg + 40):
        xp = 200
        yp = 380
    if (200 < yp < 250) and (pos_xp - 10 < xp < pos_xp + 40):
        xp = 200
        yp = 380
    if (140 < yp < 190) and (pos_xy - 10 < xp < pos_xy + 40):
        xp = 200
        yp = 380
    if (100 < yp < 150) and (pos_xr - 10 < xp < pos_xr + 40):
        xp = 200
        yp = 380
    if (50 < yp < 110) and (pos_x - 10 < xp < pos_x + 40):
        xp = 200
        yp = 380
    clock.tick(fps)
    pygame.display.flip()

pygame.quit()
