import pygame,sys, math, random

pygame.init()

W, H = 1440, 720
screen = pygame.display.set_mode((W,H), pygame.FULLSCREEN)

def terminate():
    pygame.quit()
    sys.exit()

def waitForKeyOrClick():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    terminate()
                else:
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

#Draws a simple square spiral recursively
def drawSpiral(screen, x, y, length, d):
    if length > 0:
        if d == 1:
            pygame.draw.line(screen, (0,0,0), (x, y), (x+length, y))
            drawSpiral(screen, x+length, y, length-2, 2)
        elif d == 2:
            pygame.draw.line(screen, (0,0,0), (x, y), (x, y+length))
            drawSpiral(screen, x, y+length, length-2, 3)
            
        elif d == 3:
            pygame.draw.line(screen, (0,0,0), (x, y), (x-length, y))
            drawSpiral(screen, x-length, y, length-2, 4)
        else:
            pygame.draw.line(screen, (0,0,0), (x, y), (x, y-length))
            drawSpiral(screen, x, y-length, length-2, 1)

#Draws a simple tree recursively
def drawTree(screen, x, y, length, angle, color, wid):
    if length > 20:
        dec = 2
        ex = x + length*math.cos(angle)
        ey = y + length*math.sin(angle)
        newColor = None
        if length < 20:
            newColor = (220, 245, 0)
        elif length < 70:
            newColor = ( 0, min(color[1]+30,255), color[2])
        else:
            newColor = ( max(0,color[0]-5), min(color[1],255), color[2])
        pygame.draw.line(screen, color, (x, y), (ex, ey), wid)

        angle_div = 12.0
        branch_angle = random.random()*3.0 + 3
        
        drawTree(screen, ex, ey, length-10, angle+math.pi/angle_div,newColor, max(1, wid-dec))
        for i in range(3):
            if random.randint(1,2)==1: 
                drawTree(screen, ex, ey, length-10, angle+math.pi/branch_angle,newColor,max(1, wid-dec))
            else:
                drawTree(screen, ex, ey, length-10, angle-math.pi/branch_angle,newColor,max(1, wid-dec))
        drawTree(screen, ex, ey, length-10, angle-math.pi/angle_div,newColor,max(1, wid-dec))


bg_img = pygame.image.load("bg.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
    screen.blit(bg_img,(0,0))
    for i in range(4):
        drawTree(screen, 100+300*i, H-100, 80, -math.pi/2.0, (139,69,19), 15)
    for i in range(4):
        drawTree(screen, 200+300*i, H-100, 80, -math.pi/2.0, (139,69,19), 15)
    pygame.display.update()
    waitForKeyOrClick()
terminate()
