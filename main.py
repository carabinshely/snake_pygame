import pygame


pygame.init()

dis = pygame.display.set_mode((500, 400))

pygame.display.update()
pygame.display.set_caption("Little snake")

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)

pygame.quit()

quit()
