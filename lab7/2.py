import pygame
from pygame import mixer 
pygame.init()
mixer.init()


#screen
screen = pygame.display.set_mode((400, 600))

#init music and arts
s1 =  "2/music/1.mp3"
s2 =  "2/music/2.mp3"
s3 =  "2/music/3.mp3"
s4 =  "2/music/4.mp3"
s5 =  "2/music/5.mp3"
art1 = pygame.image.load("2/icons/a1.jpg")
art2 = pygame.image.load("2/icons/a2.jpg")
art3 = pygame.image.load("2/icons/a3.jpg")
art4 = pygame.image.load("2/icons/a4.jpg")
art5 = pygame.image.load("2/icons/a5.jpg")

art_cor = (0, 0)
pl = []
arts = [art1, art2, art3, art4, art5]
id_of_art = 0

def insert_into_playlist(playlist, music_file): 
    playlist.append(music_file)

#inserting music into playlist
insert_into_playlist(pl, s1)
insert_into_playlist(pl, s2)
insert_into_playlist(pl, s3)
insert_into_playlist(pl, s4)
insert_into_playlist(pl, s5)
  
def play_music(playList, i = 0):
    pygame.mixer.music.load(playList[i])
    pygame.mixer.music.play() 

#SET LOGO AND TITLE
pygame.display.set_caption("MP3 Player")
icon = pygame.image.load("2/icons/p.png")
pygame.display.set_icon(icon)

#another 2/icons and their coordinates
pause = pygame.image.load("2/icons/pause.png")
pause_cor = (170, 500)
play = pygame.image.load("2/icons/play.png")
play_cor = (170, 500)
next_song = pygame.image.load("2/icons/next.png")
next_cor = (270, 500)
prev = pygame.image.load("2/icons/back.png")
prev_cor = (70, 500)
sq = pygame.image.load("2/icons/square.png")

#draw img on screen
def draw(img, cor):
    screen.blit(img, cor)

#boolean for check is pause
is_pause = False

#fill display in white
screen.fill((255,255,255))

#drawing buttons
draw(next_song, next_cor)
draw(prev, prev_cor)
draw(play, play_cor)

#queqe of music from 0
music_id = 0

cur_img = play
first_play = True

#GAME LOOP
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                screen.fill((255,255,255))
                if first_play:
                    cur_img = pause
                    is_pause = False
                    play_music(pl, music_id)
                    draw(arts[id_of_art], art_cor)
                    first_play = False
                elif is_pause:
                    cur_img = pause
                    is_pause = False
                    mixer.music.unpause() 
                else:
                    cur_img = play
                    is_pause = True
                    mixer.music.pause()
            if key[pygame.K_RIGHT]:
                screen.fill((255,255,255))
                if first_play:
                    cur_img = pause
                    is_pause = False
                    play_music(pl, music_id)
                    first_play = False
                else:
                    mixer.music.stop()
                    screen.fill((255,255,255))
                    if music_id == 4:
                        music_id = 0
                        id_of_art = 0
                    else: 
                        music_id += 1
                        id_of_art += 1
                    play_music(pl, music_id)
            if key[pygame.K_LEFT]:
                if first_play:
                    cur_img = pause
                    is_pause = False
                    play_music(pl, music_id)
                    first_play = False
                else:
                    mixer.music.stop()
                    screen.fill((255,255,255))
                    if music_id == 0:
                        music_id = 4
                        id_of_art = 4
                    else:
                        music_id -= 1
                        id_of_art -= 1
                    play_music(pl, music_id)
            draw(arts[id_of_art], art_cor)
            draw(cur_img, pause_cor)
            draw(next_song, next_cor)
            draw(prev, prev_cor)

    pygame.display.update()
