import pygame
pygame.init()

#screen
screen = pygame.display.set_mode((1400, 700))
screen.fill((255,255,255))
run = True
ball_x = 700
ball_y = 350
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                if ball_x < 1365:
                    ball_x += 20
            if key[pygame.K_LEFT]:
                if ball_x > 35:
                    ball_x -= 20
            if key[pygame.K_UP]:
                if ball_y > 30:
                    ball_y -= 20
            if key[pygame.K_DOWN]:
                if ball_y < 670:
                    ball_y += 20
        screen.fill((255,255,255))
        pygame.draw.circle(screen, (255,0,0),(ball_x, ball_y), 25)
        pygame.display.update()
