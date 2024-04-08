import pygame
import time
import random
 
pygame.init()

# Randomly generating food with different weights
# Foods which are disappearing after some time(timer)
# Comment your code

#idenntifying some colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#setting our display
dis_width = 600
dis_height = 400

#creating title and surface
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

#size and speed of snake
snake_block = 10
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 25)

#scores
score = 0
collected = True
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, (0, 0))

def your_level(score):
    lvl = score_font.render("Your Level: " + str(int(score/4)), True, yellow)
    dis.blit(lvl, (420, 0))

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
def gameLoop():
    global score  # Adding this line to ensure that score is treated as a global variable

    game_over = False
    game_close = False

    score = 0  # Initialize score here

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    start_time = round(time.time())

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            your_level(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #checking and deleting the food if it wasnot collected in 10sec after his appear
        is_collected = False
        global collected
        if not is_collected:
            cur_time = round(time.time())
            if collected:
                start_time = cur_time
                collected = False
            else:
                if cur_time == start_time + 10:
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                    start_time = cur_time

        #kill if snake touch the borders
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        #printing our scores
        our_snake(snake_block, snake_List)
        Your_score(score)
        your_level(score)

        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += random.randint(1, 5)
            collected = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
