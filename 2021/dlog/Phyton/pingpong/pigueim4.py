import sys, pygame
pygame.init()
size=1000, 800
screen=pygame.display.set_mode(size)
pygame.display.set_caption("pelota rebotadora")
width, height=1000, 800
speed=[2,2]
color=255, 255, 255
ball=pygame.image.load("N:\D.Log 2\Burbuja 1\Ibanez Mateo\_tenis.png")
obstaculo=pygame.image.load("N:\D.Log 2\Burbuja 1\Ibanez Mateo\__tenis.png")
obstaculo2=pygame.image.load("N:\D.Log 2\Burbuja 1\Ibanez Mateo\__tenis.png")
ballrect=ball.get_rect()
obstaculorect=obstaculo.get_rect()
obstaculo2rect=obstaculo2.get_rect()
run=True

ballrect.move_ip(700, 400)
obstaculorect.move_ip(0, 400)
obstaculo2rect.move_ip(1000, 400)
while run:
    pygame.time.delay(2)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:run=False

 
    keys=pygame.key.get_pressed()     
    if keys[pygame.K_w]:
        obstaculorect=obstaculorect.move(0, -1)
    if keys[pygame.K_s]:
        obstaculorect=obstaculorect.move(0, 1)

    keys=pygame.key.get_pressed()     
    if keys[pygame.K_UP]:
        obstaculo2rect=obstaculo2rect.move(0, -1)
    if keys[pygame.K_DOWN]:
        obstaculo2rect=obstaculo2rect.move(0, 1)
        

    if obstaculorect.colliderect(ballrect):
        speed[0]=-speed[0]

    if obstaculo2rect.colliderect(ballrect):
        speed[0]=-speed[0]


    ballrect=ballrect.move(speed)  
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]         
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]


    screen.fill(color)
    screen.blit(ball, ballrect)
    screen.blit(obstaculo, obstaculorect)
    screen.blit(obstaculo2, obstaculo2rect)
    pygame.display.flip()


pygame.QUIT()
