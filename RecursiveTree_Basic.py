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


#Draws a simple tree recursively
def drawTree(screen, x, y, length, angle, color, wid,div):
    if length > 5:
        ex = x + length*math.cos(angle)
        ey = y + length*math.sin(angle)
        pygame.draw.line(screen, color, (x, y), (ex, ey), wid)
        drawTree(screen, ex, ey, length-10, angle+math.pi/div,color, wid, div)
        drawTree(screen, ex, ey, length-10, angle-math.pi/div,color, wid, div)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                terminate()
    screen.fill((255,255,255))

    
    drawTree(screen, W/2, H-100, 80, -math.pi/2.0, (0,0,0), 3, 6.0)

    pygame.display.update()
    clock.tick(30)
terminate()
