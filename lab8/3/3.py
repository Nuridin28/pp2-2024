import pygame
import math

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint")

    drawing = False
    shape = "circle"  # Изначально выбрано рисование кругов
    start_pos = (0, 0)
    color = BLACK
    brush_size = 5
    eraser_size = 20

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши - начать рисование
                    drawing = True
                    start_pos = event.pos
                elif event.button == 3:  # Правая кнопка мыши - заливка цветом
                    fill_color(screen, color)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Левая кнопка мыши - закончить рисование
                    drawing = False
                    if shape == "circle":
                        draw_circle(screen, start_pos, pygame.mouse.get_pos(), color)
                    elif shape == "rect":
                        draw_rect(screen, start_pos, pygame.mouse.get_pos(), color)
                    elif shape == "eraser":
                        draw_eraser(screen, start_pos, pygame.mouse.get_pos(), eraser_size)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Нажата клавиша R - выбрать красный цвет
                    color = RED
                elif event.key == pygame.K_g:  # Нажата клавиша G - выбрать зеленый цвет
                    color = GREEN
                elif event.key == pygame.K_b:  # Нажата клавиша B - выбрать синий цвет
                    color = BLUE
                elif event.key == pygame.K_w:  # Нажата клавиша W - выбрать белый цвет
                    color = WHITE
                elif event.key == pygame.K_UP:  # Нажата клавиша  UP - выбрать режим рисования кругов
                    shape = "circle"
                elif event.key == pygame.K_DOWN:  # Нажата клавиша DOWN - выбрать режим рисования прямоугольников
                    shape = "rect"
                elif event.key == pygame.K_e:  # Нажата клавиша E - выбрать режим стирки
                    shape = "eraser"
                elif event.key == pygame.K_LEFT:  # Нажата клавиша LEFT - выбрать режим кисти
                    shape = "brush"
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    if shape == "brush":
                        draw_brush(screen, event.pos, color, brush_size)
                    elif shape == "eraser":
                        draw_eraser(screen, event.pos, color, eraser_size)

        pygame.display.flip()

def draw_circle(screen, start_pos, end_pos, color):
    radius = int(math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))
    pygame.draw.circle(screen, color, start_pos, radius, 2)

def draw_rect(screen, start_pos, end_pos, color):
    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    pygame.draw.rect(screen, color, rect, 2)

def draw_brush(screen, pos, color, size):
    pygame.draw.circle(screen, color, pos, size)

def draw_eraser(screen, start_pos, end_pos, size):
    rect = pygame.Rect(start_pos[0] - size/2, start_pos[1] - size/2, size, size)
    pygame.draw.rect(screen, WHITE, rect)

def fill_color(screen, color):
    screen.fill(color)

if __name__ == "__main__":
    main()
