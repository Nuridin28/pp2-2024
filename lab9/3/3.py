import pygame
import math

# Colors
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
    shape = "circle"  # Initially set to draw circles
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
                if event.button == 1:  # Left mouse button - start drawing
                    drawing = True
                    start_pos = event.pos
                elif event.button == 3:  # Right mouse button - fill with color
                    fill_color(screen, color)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button - stop drawing
                    drawing = False
                    if shape == "circle":
                        draw_circle(screen, start_pos, pygame.mouse.get_pos(), color)
                    elif shape == "rect":
                        draw_rect(screen, start_pos, pygame.mouse.get_pos(), color)
                    elif shape == "eraser":
                        draw_eraser(screen, start_pos, pygame.mouse.get_pos(), eraser_size)
                    elif shape == "square":
                        draw_square(screen, start_pos, pygame.mouse.get_pos(), color)
                    elif shape == "right_triangle":
                        draw_right_triangle(screen, start_pos, pygame.mouse.get_pos(), color)
                    elif shape == "equilateral_triangle":
                        draw_equilateral_triangle(screen, start_pos, pygame.mouse.get_pos(), color)
                    elif shape == "rhombus":
                        draw_rhombus(screen, start_pos, pygame.mouse.get_pos(), color)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # R key - set color to red
                    color = RED
                elif event.key == pygame.K_g:  # G key - set color to green
                    color = GREEN
                elif event.key == pygame.K_b:  # B key - set color to blue
                    color = BLUE
                elif event.key == pygame.K_w:  # W key - set color to white
                    color = WHITE
                elif event.key == pygame.K_UP:  # UP key - set shape to draw circles
                    shape = "circle"
                elif event.key == pygame.K_DOWN:  # DOWN key - set shape to draw rectangles
                    shape = "rect"
                elif event.key == pygame.K_e:  # E key - set shape to eraser
                    shape = "eraser"
                elif event.key == pygame.K_s:  # S key - set shape to draw squares
                    shape = "square"
                elif event.key == pygame.K_t:  # T key - set shape to draw right triangles
                    shape = "right_triangle"
                elif event.key == pygame.K_q:  # Q key - set shape to draw equilateral triangles
                    shape = "equilateral_triangle"
                elif event.key == pygame.K_h:  # H key - set shape to draw rhombus
                    shape = "rhombus"
                elif event.key == pygame.K_LEFT:  # LEFT key - set shape to brush
                    shape = "brush"
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    if shape == "brush":
                        draw_brush(screen, event.pos, color, brush_size)
                    elif shape == "eraser":
                        draw_eraser(screen, event.pos, color, eraser_size)

        pygame.display.flip()

# Function to draw a circle
def draw_circle(screen, start_pos, end_pos, color):
    radius = int(math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))
    pygame.draw.circle(screen, color, start_pos, radius, 2)

# Function to draw a rectangle
def draw_rect(screen, start_pos, end_pos, color):
    rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
    pygame.draw.rect(screen, color, rect, 2)

# Function to draw a square
def draw_square(screen, start_pos, end_pos, color):
    side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
    square_rect = pygame.Rect(start_pos[0], start_pos[1], side_length, side_length)
    pygame.draw.rect(screen, color, square_rect, 2)

# Function to draw a right triangle
def draw_right_triangle(screen, start_pos, end_pos, color):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    points = [(start_pos[0], start_pos[1]), (start_pos[0], start_pos[1] + dy), (start_pos[0] + dx, start_pos[1] + dy)]
    pygame.draw.polygon(screen, color, points, 2)

# Function to draw an equilateral triangle
def draw_equilateral_triangle(screen, start_pos, end_pos, color):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    height = math.sqrt(3) * dx / 2  # Height of an equilateral triangle
    points = [(start_pos[0], start_pos[1]), (start_pos[0] + dx / 2, start_pos[1] + height), (start_pos[0] + dx, start_pos[1])]
    pygame.draw.polygon(screen, color, points, 2)

# Function to draw a rhombus
def draw_rhombus(screen, start_pos, end_pos, color):
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    points = [(start_pos[0] + dx / 2, start_pos[1]), (end_pos[0], start_pos[1] + dy / 2),
              (start_pos[0] + dx / 2, end_pos[1]), (start_pos[0], start_pos[1] + dy / 2)]
    pygame.draw.polygon(screen, color, points, 2)

# Function to draw a brush
def draw_brush(screen, pos, color, size):
    pygame.draw.circle(screen, color, pos, size)

# Function to draw an eraser
def draw_eraser(screen, start_pos, end_pos, size):
    rect = pygame.Rect(start_pos[0] - size / 2, start_pos[1] - size / 2, size, size)
    pygame.draw.rect(screen, WHITE, rect)

# Function to fill the screen with color
def fill_color(screen, color):
    screen.fill(color)

if __name__ == "__main__":
    main()
