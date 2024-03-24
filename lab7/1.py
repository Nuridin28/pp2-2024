import pygame
import math
from datetime import datetime

WIDTH, HEIGHT = 1200, 800
RADIUS = 300
X, Y = 600, 400

pygame.init()

surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))
clock12 = dict(zip(range(12), range(0, 360, 30)))

def print_text(text, pos):
    font = pygame.font.SysFont("Georgia", 50, True, False)
    surface2 = font.render(text, True, (0,0,255))
    surface.blit(surface2, pos)

def get_sec_pos(clock_dict, clock_hand):
    x = X+RADIUS*math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = Y+RADIUS*math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x,y

def get_min_pos(clock_dict, clock_hand):
    x = X+RADIUS*math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2) - 60
    y = Y+RADIUS*math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2) - 60
    return x,y

def get_hour_pos(clock_dict, clock_hand):
    x = X+RADIUS*math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = Y+RADIUS*math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2) 
    return x,y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    #set bg
    surface.fill(pygame.Color('black'))

    #get time

    t = datetime.now()

    hour, minute, second = t.hour%12, t.minute, t.second

    #draw clock

    pygame.draw.circle(surface, (255, 255, 255), (X, Y) , RADIUS+50)
    pygame.draw.line(surface, (0,0,0), (600, 400), get_sec_pos(clock60, second))
    pygame.draw.line(surface, (255,0,0), (600, 400), get_min_pos(clock60, minute-3))
    print_text(str(12), get_hour_pos(clock12, 0))
    for i in range(1, 12):
        print_text(str(i), get_hour_pos(clock12, i))

    pygame.display.flip()
    clock.tick(20)

