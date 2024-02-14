from maps import *


if __name__ == '__main__':
    pygame.init()
    size = width, heigth = (800, 450)
    screen = pygame.display.set_mode((width, heigth))
    running = True
    MMM = Map(0, 0, screen)
    Type = 0
    var = ['map', 'sat', 'sat,skl']
    while running:
        screen.fill((130, 25, 75))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.MOUSEBUTTONDOWN:
             #   MMM.Point(pos[0], pos[1])
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            MMM.update(0, -1)
            print('Up')
        elif key[pygame.K_TAB]:
            Type += 1
            if Type > 2:
                Type = 0
            MMM.stile = var[Type]
            MMM.update(0, 0)
        elif key[pygame.K_DOWN]:
            MMM.update(0, 1)
            print('Down')
        elif key[pygame.K_RIGHT]:
            MMM.update(1, 0)
            print('Right')
        elif key[pygame.K_LEFT]:
            MMM.update(-1, 0)
            print('Left')
        elif key[pygame.K_1]:
            MMM.zooming(1)
        elif key[pygame.K_2]:
            MMM.zooming(2)
        elif key[pygame.K_3]:
            MMM.zooming(3)
        elif key[pygame.K_4]:
            MMM.zooming(4)
        elif key[pygame.K_5]:
            MMM.zooming(5)
        elif key[pygame.K_6]:
            MMM.zooming(6)
        elif key[pygame.K_7]:
            MMM.zooming(7)
        elif key[pygame.K_8]:
            MMM.zooming(8)


        MMM.draw()
        pygame.display.update()
        pygame.display.flip()
    pygame.quit()