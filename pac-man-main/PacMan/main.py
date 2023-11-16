import pygame

pygame.init()

width = 800
height = 800

screen = pygame.display.set_mode((width, height))

pygame.draw.circle(screen, (0, 255, 0), (400, 400), 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()


