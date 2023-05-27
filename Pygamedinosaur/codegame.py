import pygame
import time
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Khủng long game")

# create cửa sổ game
screen = pygame.display.set_mode((600,300))

bg = pygame.image.load(r'Pygamedinosaur\resource\background.jpg')
tree = pygame.image.load(r'Pygamedinosaur\resource\tree.png')
dino = pygame.image.load(r'Pygamedinosaur\resource\dinosaur.png')

bg_x = 0
tree_x = 550
dino_y = 230

#Vòng lặp xử lý game
check = True
start_jump=0
while check:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            check = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if (dino_y == 230):
                    dino_y -= 133
            

    bg_hcn = screen.blit(bg,(bg_x,0))
    bg_hcn2 = screen.blit(bg,(bg_x+600,300))
    bg_x -= 5 #Tốc độ màn hình giật ngang
    if bg_x == -600:
        bg_x = 0
    castus = screen.blit(tree,(tree_x,230))
    tree_x -= 5
    if tree_x == 0:
        tree_x = 550
    dino_run = screen.blit(dino,(0,dino_y))
    if(start_jump != 0 ):
        end_jump=time.time()
        dino_y+=7
        #print(end_jump-start_jump)
        if(end_jump - start_jump > 0.3):
            dino_y=230
            start_jump=0
    pygame.display.update()
    if(dino_y==97 and start_jump==0):
        start_jump = time.time();
