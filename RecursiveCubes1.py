'''


Author: Jon Janelle
Modified: 1/22/2017
'''

import pygame,sys, math, random

pygame.init()
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
LIGHTBLUE = (132,112,255)
GRAY = (100,100,100)
CORAL = (240,128,128)
COLORS = [BLACK, LIGHTBLUE, CORAL, GRAY, RED, GREEN, BLUE, YELLOW, CYAN]
W, H = 1000, 600
screen = pygame.display.set_mode((W,H))

def terminate():
    pygame.quit()
    sys.exit()

            
#convert degrees to radians
def rad(degrees):
    return degrees*math.pi/180.0


#Draw a hexagon
def drawHexagon(screen, x, y, sideLen, firstAngle, offset):

    if (sideLen>5):
        angle = 0
        cx = x-math.sqrt(3)*sideLen/2.0
        cy = y+sideLen/2.0
        points = []
        for i in range(6):
            if i==0:
                angle+=firstAngle
            else:
                angle+=60
            ex = x + sideLen*math.cos(rad(angle))
            ey = y + sideLen*math.sin(rad(angle))
            points.append([ex,ey])
            #pygame.draw.circle(screen, COLORS[i], (int(x), int(y)), 5)
            x = ex
            y = ey
        
        
        for i in range(3):
            temp =[]
            for j in range(3):
                temp.append(points[(2*i+j-offset)%6])
            temp.append([cx, cy])
            
            pygame.draw.polygon(screen,COLORS[i], temp)

        drawHexagon(screen, points[2][0], points[2][1],sideLen/2,90,offset)
        drawHexagon(screen, points[3][0], points[3][1],sideLen/2,90,offset)
       
#Begin main program loop
offset = 0
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
            elif event.type == pygame.QUIT:
                terminate()
    
    screen.fill((255,255,255))
    #offset = (offset+5)%6
    drawHexagon(screen, 3*W/4, H*.4, 150,90, offset)
    #pygame.draw.line(screen, (255,0,0), (W/2+100, H*.4-75), (W/2+100, H*.4+225))
    pygame.display.update()
    clock.tick(7)
