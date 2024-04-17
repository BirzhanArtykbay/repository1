import pygame
pygame.init()

width = height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Circle')

x = y = 25
v = 10
radius = 25
color = (255, 0, 0)
doo = 1
clock = pygame.time.Clock()
is_blue = False
while doo:
    win.fill((255, 255, 255))
    for event in pygame.event.get():
                if event.type == pygame.QUIT: doo = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
                        
    keys = pygame.key.get_pressed()
    

    if is_blue: 
        color = (0, 128, 255)
        if(keys[pygame.K_a] and x-radius>=v): x-=v 
        if(keys[pygame.K_d] and x+radius+v <= width): x+=v 
        if(keys[pygame.K_w] and y>=v+radius): y-=v 
        if(keys[pygame.K_s] and y+radius+v <= height): y+=v 
    else: 
        color = (255, 100, 0)
        if(keys[pygame.K_LEFT] and x-radius>=v): x-=v + 20
        if(keys[pygame.K_RIGHT] and x+radius+v <= width): x+=v + 20
        if(keys[pygame.K_UP] and y>=v+radius): y-=v + 20
        if(keys[pygame.K_DOWN] and y+radius+v <= height): y+=v + 20
        
    pygame.draw.circle(win, color, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)