import sys, pygame
pygame.init()
size=800, 600
screen=pygame.display.set_mode(size)
pygame.display.set_caption("pelota rebotadora")
width, height=900, 700
speed=[1,1]
color=255, 255, 255
ball=pygame.image.load("N:\D.Log 2\Burbuja 1\Ibanez Mateo\ulbo.png")
obstaculo=pygame.image.load("N:\D.Log 2\Burbuja 1\Ibanez Mateo\espada.png")
ballrect=ball.get_rect()
obstaculorect=obstaculo.get_rect()
run=True
obstaculo

while run:
    pygame.time.delay(2)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:run=False

 
    keys=pygame.key.get_pressed()     
    if keys[pygame.K_UP]:
        obstaculorect=obstaculorect.move(0, -1)
    if keys[pygame.K_DOWN]:
        obstaculorect=obstaculorect.move(0, 1)

    if obstaculorect.colliderect(ballrect):
        speed[0]=-speed[0]


    ballrect=ballrect.move(speed)  
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]         
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]


    screen.fill(color)
    screen.blit(ball, ballrect)
    screen.blit(obstaculo, obstaculorect)
    pygame.display.flip()


pygame.QUIT()
