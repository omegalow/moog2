from random import randint
from sys import exit

import pygame

#3/26
# class Player(pygame.sprite.Sprite):
#     def __init__(self, *groups: AbstractGroup) -> None:
#         super().__init__(*groups)
#         self.image = pygame.image.load('graphics/mooogwalk1.png').convert_alpha()
#         self.rect = self.image.get_rect(midbottom = (200,300))


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'{current_time}',False,('#afddf2'))
    score_rect = score_surface.get_rect(center = (400,150))
    screen.blit(score_surface,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 306: screen.blit(musicnote_surface,obstacle_rect)
            else: screen.blit(musicnote2_surface,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True


def player_animation():
    global player_surface, player_index

    # player_index += 0.1
    # if player_index >= len(player_walk):player_index = 0
    # player_surface = player_walk[int(player_index)]

    if player_rect.bottom <= 305:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surface = player_walk[int(player_index)]




pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('MOOOG')

clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

game_active = True

notehit = True

notehitscore = 0

start_time = 0

score = 0

sky_surface = pygame.image.load('graphics/sky2.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

# score_surface = test_font.render('MOOOG',False,'white')
# score_rect = score_surface.get_rect(center = (400,150))

#musicnote_surface = pygame.image.load('graphics/musicnote.png').convert_alpha()
#musicnote_x_pos = 600

#enemies
musicnote_surface = pygame.image.load('graphics/musicnote.png').convert_alpha()


musicnote2_surface = pygame.image.load('graphics/musicnote2.png').convert_alpha()

# note = 4

# half_note = 2

# quarter_note = 1

# eight_note = 0.5

# sixteenth_note = 0.25

# clock = pygame.time.Clock()
# spawn_counter = 2000 # milliseconds

# while running:
#   clock.tick(60)
#   spawn_counter -= clock.get_rawtime()
#   if spawn_counter <= 0:
#     spawn_enemy() 
#     spawn_counter = 2000


# spawn_counter1 = 2000 # milliseconds

# spawn_counter1 -= clock.get_rawtime()


# note_list = [4,2,1,0.5,0.25]

# beat_duration = int(note_list[randint(0, len(note_list) - 1)] * 1000)

# BPM = 60000 / beat_duration

# BPM = randint(0,160)
# BPM = BPM * 1000
# beat_duration = 60000 / BPM

BPM = randint(1,160)

BPM_surface = test_font.render(f'{BPM}', False, ('#afddf2'))

BPM_rect = BPM_surface.get_rect(center = (400,200))

beat_duration = 60000 / BPM

whole_note_duration = beat_duration * 4

half_note_duration = beat_duration * 2

eighth_note_duration = beat_duration / 2

sixteenth_note_duration = beat_duration / 4

obstacle_rect_list = []

#player
player_walk1 = pygame.image.load('graphics/mooogwalk1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/mooogwalk2.png').convert_alpha()
player_walk3 = pygame.image.load('graphics/mooogwalk3.png').convert_alpha()
player_walk = [player_walk1, player_walk2, player_walk3]
player_index = 0
player_jump = pygame.image.load('graphics/mooogwalk3.png').convert_alpha()

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80,306))
player_gravity = 0

#intro/menu screen
player_stand = pygame.image.load('graphics/moog.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('MOOOG',False,'white')
game_name_rect = game_name.get_rect(center = (400,75))

game_message = test_font.render('press space',False, 'white')
game_message_rect = game_message.get_rect(center = (400,300))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # if event.type == pygame.MOUSEMOTION:
            #     if player_rect.collidepoint(event.pos): print('collision')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # player_gravity += 1
                    # player_rect.y += player_gravity
                    player_rect.bottom = 246
                    if notehit == False:
                        notehitscore += 1

                        print(notehitscore)
                        print("nuh")
                    # player_animation()
                    # screen.blit(player_surface,player_rect)
                
                    
                if event.key == pygame.K_LSHIFT:
                    # player_gravity += 1
                    # player_rect.y += player_gravity
                    player_rect.bottom = 306
                    # player_animation()
                    # screen.blit(player_surface,player_rect)
                

                #if event.key == pygame.K_SPACE and player_rect.bottom >= 306:
                    #player_gravity = -15
        # if event.type == pygame.KEYUP:
        #     print('key up')
        else:
             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(musicnote_surface.get_rect(bottomright = (1100,306)))
            else:
                obstacle_rect_list.append(musicnote2_surface.get_rect(bottomright = (1100,246)))

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        screen.blit(BPM_surface, BPM_rect)
        # pygame.draw.rect(screen,'#afddf2',score_rect)
        # pygame.draw.rect(screen,'#afddf2',score_rect,10)
        # screen.blit(score_surface,score_rect)
        score = display_score()
        
       # musicnote_rect.x -= 4
       # if musicnote_rect.right < 0: musicnote_rect.left = 800
       # screen.blit(musicnote_surface,musicnote_rect)

        #player
        #player_gravity += 1
        #player_rect.y += player_gravity
        #player_rect.bottom = 286
        player_animation()
        screen.blit(player_surface,player_rect)

        #enemy movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision - really important for testing
        #if musicnote_rect.colliderect(player_rect):
            #game_active = False
        #game_active = collisions(player_rect, obstacle_rect_list)
        notehit = collisions(player_rect, obstacle_rect_list)
        if notehit == False:
            notehitscore += 1
            print(notehitscore)
            print("nuh")
        
        if notehitscore >= 150:
            notehitscore = 0
            game_active = False
        

    else:
        #not active part of game. menu or restart.
        screen.fill('#d8ecfa')
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,306)
        player_gravity = 0
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)
        score_name = test_font.render(f'{score}',False,'white')
        score_name_rect = score_name.get_rect(center = (400,50))
        screen.blit(score_name,score_name_rect)
        
        

        

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        #if player_rect.colliderect(musicnote_rect):
        #    print('collision')

        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())


    pygame.display.update()
    clock.tick(60)