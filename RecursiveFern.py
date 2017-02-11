'''
Recursively draw a fern-like image
*Current setting make it look a bit like a conifer
*Push the space bar to generate a new image. Hold it to make the tree "dance"

Author: Jon Janelle
Modified: 1/22/2017
'''

import pygame,sys, math, random

pygame.init()

W, H = 1440, 720
screen = pygame.display.set_mode((W,H), pygame.FULLSCREEN)

def terminate():
    pygame.quit()
    sys.exit()

            
#convert degrees to radians
def rad(degrees):
    return degrees*math.pi/180

#Draws a simple fern recursively
def drawFern(screen, x, y, length, angle, color, wid):
    if length > 1:
        ex = x + length*math.cos(angle)
        ey = y + length*math.sin(angle)

        pygame.draw.line(screen, color, (x, y), (ex, ey), wid)
        drawFern(screen, ex, ey, 0.55*length, angle+rad(random.randint(70,90)), color, int(.75*wid))
        drawFern(screen, ex, ey, 0.55*length,angle+rad(-1*random.randint(80,100)) , color,int(.75*wid))
        drawFern(screen, ex, ey, 0.70*length,angle+rad(random.randint(-5,5)) , color, int(.8*wid))

#Begin main program loop
screen.fill((255,255,255))
drawFern(screen, W/2, 3*H/4, 100, rad(-90), (0, 100, 0), 20)      
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
            elif event.type == pygame.QUIT:
                terminate()
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        screen.fill((255,255,255))
        drawFern(screen, W/2, 3*H/4, 100, rad(-90), (0, 100, 0), 20)
    pygame.display.update()

