import pygame
import random
from paddle import Paddle
from ball import Ball
white = (255,255,255)
black = (0,0,0)
green = (0,150,0)
red = (255,0,0)
blue = (0,0,255)
light_blue = (147,251,253)
pygame.init()
pygame.mixer.init()
titleFont = pygame.font.Font("Gameplay.ttf", 60)
creditsFont = pygame.font.Font("Gameplay.ttf", 30)
pygame.mixer.music.load("assets/bg music.mp3")
def titleScreen():
    title = True
    pixelated_font = pygame.font.Font('Gameplay.ttf', 10) 
    title_font = pygame.font.Font('Techno.OTF', 70)  
    
    while title:
        title_text = title_font.render("Hockeython", True, (6, 248, 252))
        instruction_text = pixelated_font.render("Press any key to start", True, white)
        screen.blit(title_text, ((screen.get_width() - title_text.get_width()) / 2, 250))
        screen.blit(instruction_text, ((screen.get_width() - instruction_text.get_width()) / 2, 350))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                title = False



BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
CYAN =(0,255,255)
MAGENTA = (255,0,255)
BLUE = (0,0,255)

size = (700, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hockeython")
 
paddleA = Paddle(RED, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(BLUE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200
 
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195
 
all_sprites_list = pygame.sprite.Group()
 
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)
 
carryOn = True
 
clock = pygame.time.Clock()
 
scoreA = 0
scoreB = 0

titleScreen()
# Start playing the music
pygame.mixer.music.play()


start_time = pygame.time.get_ticks()
countdown_duration = 60000

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q: 
                    carryOn=False
                elif event.key == pygame.K_r: 
                  pygame.mixer.music.play()
                  scoreA = 0
                  scoreB = 0
                  start_time = pygame.time.get_ticks()
                  ball.rect.x = 345
                  ball.rect.y = 195
                  ball.velocity = [random.randint(-8, -4), random.randint(-8, 8)]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(10)
    if keys[pygame.K_s]:
        paddleA.moveDown(10)
    if keys[pygame.K_UP]:
        paddleB.moveUp(10)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(10)    
 
    all_sprites_list.update()
    
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity = [random.randint(-8,-4),random.randint(-8,8)]
        ball.rect.x = 345
        ball.rect.y = 195 

    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity = [random.randint(4,8),random.randint(8,8)]
        ball.rect.x = 345
        ball.rect.y = 195 

    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1] 

    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
 

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    screen.fill(BLACK)
    
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    pygame.draw.line(screen, WHITE, [0,500], [700,500], 5)

    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    remaining_time = max(0, countdown_duration - elapsed_time)
    seconds_remaining = remaining_time // 1000
    timer_text = titleFont.render(f"Time: {seconds_remaining}", True, white)
    text_rect = timer_text.get_rect(center=(355, 550))
    screen.blit(timer_text, text_rect)
    all_sprites_list.draw(screen) 
 
   
    text = titleFont.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = titleFont.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

    
    if remaining_time == 0:

       if scoreA > scoreB:
           winner_text = titleFont.render("PLAYER 1 WINS!", True, WHITE)
       elif scoreB > scoreA:
           winner_text = titleFont.render("PLAYER 2 WINS!", True, WHITE)
       else:
            winner_text = titleFont.render("It's a Draw!", True, WHITE)
            
       screen.fill(BLACK)

       winner_rect = winner_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
       screen.blit(winner_text, winner_rect)
       restart_text = creditsFont.render("Press 'R' to restart", True, white)
       quit_text = creditsFont.render("Press 'Q' to quit", True, white)
       restart_rect = restart_text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 100))
       quit_rect = quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 50))
       screen.blit(restart_text, restart_rect)
       screen.blit(quit_text, quit_rect)
    pygame.display.flip()
    clock.tick(60)